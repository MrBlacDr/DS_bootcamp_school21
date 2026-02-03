import os
from random import randint
import logging
import requests
import json
from config import LOG_FILE, LOG_FORMAT, LOG_LEVEL, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


# Настройка логирования
logging.basicConfig(
    filename=LOG_FILE,
    format=LOG_FORMAT,
    level=getattr(logging, LOG_LEVEL)
)


class Research:
    def __init__(self, path):
        self.path = path
        self.logger = logging.getLogger(f"{__name__}.Research")
        self.logger.debug(f"Research initialized with path: {path}")
        self.chat_id = TELEGRAM_CHAT_ID
        self.bot_token = TELEGRAM_BOT_TOKEN

    class Calculations:
        def __init__(self, data):
            self.data = data
            self.logger = logging.getLogger(f"{__name__}.Research.Calculations")
            self.logger.debug("Calculations initialized")

        def counts(self):
            self.logger.info("Calculating counts of heads and tails")
            heads = sum(map(lambda x: x[0], self.data))
            tails = sum(map(lambda x: x[1], self.data))
            return heads, tails
        
        def fractions(self):
            self.logger.info("Calculating fractions of heads and tails")
            h, t = self.counts()
            total = h + t
            if total == 0:
                return 0.0, 0.0
            return h / total, t / total
    
    class Analytics(Calculations):
        def predict_random(self, num_preds):
            self.logger.info(f"Generating {num_preds} random predictions")
            preds = []
            for _ in range(num_preds):
                digit = randint(0,1)
                preds.append([digit, 1-digit])
            return preds
        
        def predict_last(self):
            self.logger.info("Predicting based on last observation")
            return self.data[-1]
        
        def save_file(self, data, file_name, postfix):
            self.logger.info(f"Saving report to {file_name}")
            with open(file_name+'.'+postfix, 'w', encoding='utf-8') as f:
                f.write(data)

    def file_reader(self, has_header=True):
        self.logger.info(f"Reading file: {self.path} with has_header={has_header}")

        if not os.path.exists(self.path):
            error_msg = f"File {self.path} does not exist"
            self.logger.error(error_msg)
            raise FileNotFoundError(error_msg)

        with open(self.path, "r") as file:
            lines = file.readlines()
        
        contents = []
        if has_header:
            header = lines[0].strip().split(',')
            if len(header) != 2:
                error_msg = "Header must contain exactly two columns separated by comma"
                self.logger.error(error_msg)
                raise Exception(error_msg)
            if header[0].strip() == '' or header[1].strip() == '':
                error_msg = "Header columns cannot be empty"
                self.logger.error(error_msg)
                raise Exception(error_msg)
            start_pos = 1
        else:
            self.logger.debug("Header skipped")
            start_pos = 0

        for i, line in enumerate(lines[start_pos:], start=start_pos+1):
            parts = line.strip().split(',')
            if len(parts) != 2:
                error_msg = f"Line {i} must contain exactly two values separated by comma"
                self.logger.error(error_msg)
                raise Exception(error_msg)
            
            try:
                val1 = parts[0].strip()
                val2 = parts[1].strip()
                
                if val1 not in ['0', '1'] or val2 not in ['0', '1']:
                    error_msg = f"Line {i}: values must be 0 or 1, got '{val1}' and '{val2}'"
                    self.logger.error(error_msg)
                    raise Exception(error_msg)
                
                if val1 == val2:
                    error_msg = f"Line {i}: values must be different (one 0 and one 1)"
                    self.logger.error(error_msg)
                    raise Exception(error_msg)
                    
            except Exception as e:
                self.logger.exception(f"Error reading file: {e}")
                raise Exception(f"Line {i}: invalid format - {e}")
            
            contents.append([int(val1), int(val2)])
        
        return contents
    
    def send_to_tg(self, has_error=False):
        if has_error:
            msg = "The report hasn't been created due to an error."
        else:
            msg = "The report has been successfully created"

        base_url = f"https://api.telegram.org/bot{self.bot_token}"
        try:            
            payload = {
                'chat_id': self.chat_id,
                'text': msg
            }
            
            # Отправляем POST запрос
            response = requests.post(
                f"{base_url}/sendMessage",
                json=payload,
                timeout=10
            )
            
            response.raise_for_status()
            
            self.logger.info(f"Telegram message sent successfully: {msg}")
            return True
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to send Telegram message: {e}")
            return False
        except Exception as e:
            self.logger.exception(f"Unexpected error sending Telegram message: {e}")
            return False
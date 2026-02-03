file_name = 'data.csv'
num_of_steps = 3
num_to_str = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}

LOG_FILE = "analytics.log"
LOG_FORMAT = '%(asctime)s %(message)s'
LOG_LEVEL = 'DEBUG'
TELEGRAM_BOT_TOKEN="1984946069:AAGMxNbCkmFdeY6dhJvwEB9z7DzrPXsZrgY"
TELEGRAM_CHAT_ID="-5185371728"

def generate_report(num_obs, tails, heads, p_t, p_h, t_forecasted, h_forecasted):
    template = f'''We made {num_obs} observations by tossing a coin: {num_to_str[tails]} were tails and {num_to_str[heads]} were heads. 
The probabilities are {(100*p_t):.2f}% and {(100*p_h):.2f}%, respectively. 
Our forecast is that the next {num_to_str[num_of_steps]} observations will be: {num_to_str[t_forecasted]} tail and {num_to_str[h_forecasted]} heads. '''
    return template
import sys
import os


class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        with open(self.path, "r") as file:
            contents = file.read()
        
        lines = contents.strip().split('\n')
        
        if len(lines) < 2:
            raise Exception("File must contain at least header and one data line")
        
        header = lines[0].split(',')
        if len(header) != 2:
            raise Exception("Header must contain exactly two columns separated by comma")
        if header[0].strip() == '' or header[1].strip() == '':
            raise Exception("Header columns cannot be empty")
        
        for i, line in enumerate(lines[1:], start=2):
            parts = line.split(',')
            if len(parts) != 2:
                raise Exception(f"Line {i} must contain exactly two values separated by comma")
            
            try:
                val1 = parts[0].strip()
                val2 = parts[1].strip()
                
                if val1 not in ['0', '1'] or val2 not in ['0', '1']:
                    raise Exception(f"Line {i}: values must be 0 or 1, got '{val1}' and '{val2}'")
                
                if val1 == val2:
                    raise Exception(f"Line {i}: values must be different (one 0 and one 1)")
                    
            except Exception as e:
                raise Exception(f"Line {i}: invalid format - {e}")
        
        return contents


def get_and_check():
    given_args = len(sys.argv)
    file_path = ''
    if given_args == 2:
        file_path = sys.argv[1]
    else:
        if given_args > 2:
            raise Exception("to many arguments")
        else:
            raise Exception("programm takes at least 1 argument - file_path")

    if os.path.exists(file_path):
        return file_path
    raise Exception(f"file {file_path} does not exists")


def main():
    try:
        file_path = get_and_check()
        research = Research(file_path)
        print(research.file_reader())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
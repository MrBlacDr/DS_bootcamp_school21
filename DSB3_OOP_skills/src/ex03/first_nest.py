import sys
import os


class Research:
    def __init__(self, path):
        self.path = path

    class Calculations:
        def counts(data):
            heads = sum(map(lambda x: x[0], data))
            tails = sum(map(lambda x: x[1], data))
            return heads, tails
        
        def fractions(h, t):
            total = h + t
            if total == 0:
                return 0.0, 0.0
            return h / total, t / total

    def file_reader(self, has_header=True):
        with open(self.path, "r") as file:
            lines = file.readlines()
        
        contents = []
        if has_header:
            header = lines[0].strip().split(',')
            if len(header) != 2:
                raise Exception("Header must contain exactly two columns separated by comma")
            if header[0].strip() == '' or header[1].strip() == '':
                raise Exception("Header columns cannot be empty")
            start_pos = 1
        else:
            start_pos = 0

        for i, line in enumerate(lines[start_pos:], start=start_pos+1):
            parts = line.strip().split(',')
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
            
            contents.append([int(val1), int(val2)])
        
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
        data = research.file_reader()
        print(data)
        heads, tails = research.Calculations.counts(data)
        print(heads, tails)
        print('{:.4f} {:.4f}'.format(*research.Calculations.fractions(heads, tails)))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
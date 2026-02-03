import sys


def prepare_letter(name):
    letter = f"Dear {name}, welcome to our team!\nWe are sure that it will be a pleasure to work with you.\nThat's a precondition for the professionals that our company hires."
    return letter


def main():
    if len(sys.argv) != 2:
        return

    email = sys.argv[1]

    with open('employees.tsv', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        s = line.strip().split('\t')
        if s[2].strip('"') == email:
            print(prepare_letter(s[0].strip('"')))
            return
    
    print('no email mathced')


if __name__ == "__main__":
    main()
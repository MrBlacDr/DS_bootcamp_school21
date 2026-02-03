import sys

def main():
    if len(sys.argv) != 2:
        return

    file_path = sys.argv[1]

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open('employees.tsv', 'w', encoding='utf-8') as f:
        f.write('"Name"\t"Surname"\t"E-mail"\n')
        for line in lines:
            email = line.strip()
            name, surname = email[:email.find('@')].split('.')
            name = '"' + name[0].upper() + name[1:] + '"'
            surname = '"' + surname[0].upper() + surname[1:] + '"'
            email = '"' + email + '"'
            res = [name, surname, email]
            tsv_line = '\t'.join(res)
            f.write(tsv_line + '\n')


if __name__ == "__main__":
    main()
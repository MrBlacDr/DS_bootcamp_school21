def convert_line_to_tsv(line):

    result = []
    current_field = []
    in_quotes = False
    i = 0
    
    while i < len(line):
        char = line[i]
        
        if char == '"':
            if i + 1 < len(line) and line[i + 1] == '"':
                # Обработка пустых кавычек ("")
                current_field.append('"')
                i += 2
                continue
            else:
                in_quotes = not in_quotes
                current_field.append(char)
        elif char == ',' and not in_quotes:
            result.append(''.join(current_field))
            current_field = []
        else:
            current_field.append(char)
        
        i += 1
    
    if current_field:
        result.append(''.join(current_field))
    
    return '\t'.join(result)

def convert_csv_to_tsv(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in lines:
                line = line.rstrip('\n')
                tsv_line = convert_line_to_tsv(line)
                f.write(tsv_line + '\n')
        
        print(f"Successfully converted {input_file} to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    
    # input_csv = '../../../DS_Bootcamp.Day00-1/src/ex02/hh_sorted.csv'
    input_csv = "ds.csv"
    output_tsv = "ds.tsv"
    
    convert_csv_to_tsv(input_csv, output_tsv)

if __name__ == "__main__":
    main()
import sys


def main():
    if len(sys.argv) != 4:
        raise Exception("Usage: python3 caesar.py <encode|decode> <text> <shift>")
    
    mode = sys.argv[1]
    text = sys.argv[2]
    
    if mode != 'encode' and mode != 'decode':
        print('Enter correct mode')
        return

    for char in text:
        if ord('А') <= ord(char) <= ord('я'):
            print("The script does not support your language yet.")
            return
    
    try:
        shift = int(sys.argv[3])
    except:
        print("Shift must be an integer")
        return
    
    result = []
    
    for char in text:
        if 'a' <= char <= 'z':
            base = ord('a')
            if mode == 'encode':
                new_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                new_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            base = ord('A')
            if mode == 'encode':
                new_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                new_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)
    
    print(''.join(result))

if __name__ == "__main__":
    main()
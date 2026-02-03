class Must_Read:
    with open("data.csv", "r") as file:
        contents = file.read()
        print(contents)


if __name__ == '__main__':
    pass
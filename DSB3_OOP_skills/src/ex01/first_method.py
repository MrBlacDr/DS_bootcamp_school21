class Research:
    def file_reader(self):
        with open("data.csv", "r") as file:
            contents = file.read()
        return contents


if __name__ == '__main__':
    print(Research().file_reader())
import os


def main():
    try:
        path = os.environ["VIRTUAL_ENV"]
        print(f"Your current virtual env is {path}")
    except KeyError:
        print('Virtual environment not found')

if __name__ == "__main__":
    main()
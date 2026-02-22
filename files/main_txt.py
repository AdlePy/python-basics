from pathlib import Path

FILE_PATH = Path(__file__).parent / "file.txt"


def main():
    with open(FILE_PATH, "w") as f:
        f.write("hello\n")

    with open(FILE_PATH, "a") as f:
        f.write("my name is python\n")

    with open(FILE_PATH, "r") as f:
        print(f.readlines())


if __name__ == "__main__":
    main()

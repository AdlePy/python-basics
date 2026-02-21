import os

IS_WINDOWS = "nt" in os.name
BASE_DIR = os.path.dirname(__file__)


def demo_paths():
    print(f"base directory: {BASE_DIR}")
    print(f"is windows: {IS_WINDOWS}")
    print(f"path separator: {os.path.sep}")

    folder_name = "pictures"
    file_name = "cat.jpg"
    print(os.path.join(BASE_DIR, folder_name, file_name))


def demo_cwd():
    cwd = os.getcwd()
    print(f"current directory: {cwd}")


def demo_list_dir():
    directory_content = os.listdir(".")
    print(f"directory content: {directory_content}")

    with open(os.path.join(BASE_DIR, "file.txt"), "w") as f:
        f.write("name: Askar Adilet\n")
        f.write("age: 29")

    if os.path.isfile(os.path.join(BASE_DIR, "file.txt")):
        os.remove(os.path.join(BASE_DIR, "file.txt"))

    with open(os.path.join(BASE_DIR, "file.txt"), "w") as f:
        f.write("name: Askar Adilet\n")
        f.write("age: 29")

    with open(os.path.join(BASE_DIR, "file.txt"), "r") as f:
        print(f.readlines())


def main():
    print("Hello main os_module!")
    demo_paths()
    demo_cwd()
    demo_list_dir()


if __name__ == "__main__":
    main()

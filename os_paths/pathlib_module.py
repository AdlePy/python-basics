from pathlib import Path


def demo_cwd():
    cwd = Path.cwd()
    print(f"current working directory: {cwd}")
    print(f"file: {Path(__file__)}")

    for path in cwd.iterdir():
        print(f"{path.name}, {path.is_dir()}, {path.is_file()}")


def demo_home():
    print(f"home directory: {Path.home()}")


def demo_check_existence():
    users = Path("/Users")
    print(f"exists: {users.exists()}")


def demo_paths():
    current_file = Path(__file__)
    print(f"current file: {current_file}")

    base_dir = current_file.parent
    print(f"base directory: {base_dir}")


def demo_build_paths():
    current_file = Path(__file__)
    base_dir = current_file.parent
    folder_name = "pictures"
    file_name = "cats.jpg"
    cats_filepath = base_dir / folder_name / file_name
    print(f"path: {cats_filepath}")


def main():
    demo_cwd()
    demo_home()
    demo_check_existence()
    demo_paths()
    demo_build_paths()


if __name__ == "__main__":
    main()

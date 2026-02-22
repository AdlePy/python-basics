import json
from pathlib import Path


JSON_FILE_PATH = Path(__file__).parent / "file.json"


def json_dump_to_string():
    data = {
        "users": [
            {"id": 42, "username": "john"},
            {"id": 43, "username": "sam"},
        ]
    }

    data_string = json.dumps(data)
    print(data_string)


def json_load_string():
    data_string = (
        '{"users": [{"id": 42, "username": "john"}, {"id": 43, "username": "sam"}]}'
    )
    data = json.loads(data_string)
    print(data)


def json_dump_to_file():
    data = {
        "users": [
            {"id": 42, "username": "john"},
            {"id": 43, "username": "sam"},
        ]
    }

    with open(JSON_FILE_PATH, "w") as f:
        json.dump(data, f)


def json_load_from_file():
    with open(JSON_FILE_PATH, "r") as f:
        data = json.load(f)

    print(data)


def main():
    # json_dump_to_string()
    # json_load_string()
    # json_dump_to_file()
    json_load_from_file()


if __name__ == "__main__":
    main()

from pathlib import Path
import configparser


CONFIG_FILE_PATH = Path(__file__).parent / "config.ini"


def config_read():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH)
    print(config.sections())
    config["smtp"]["gmail"] = "askaradilet41@gmail.com"

    with open(CONFIG_FILE_PATH, "w") as f:
        config.write(f)


def main():
    config_read()


if __name__ == "__main__":
    main()

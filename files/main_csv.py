import csv
from pathlib import Path


CSV_FILE_PATH = Path(__file__).parent / "cars.csv"


def read_csv_cars():
    with open(CSV_FILE_PATH, "r") as f:
        csv_reader = csv.reader(f, delimiter=",")

        for line in csv_reader:
            print(line)


def read_csv_as_dict():
    with open(CSV_FILE_PATH, "r") as f:
        csv_reader = csv.DictReader(f, delimiter=",")
        print(f"headers: {csv_reader.fieldnames}")

        for line in csv_reader:
            print(line)


def write_csv_dict():
    with open(CSV_FILE_PATH, "w") as f:
        csv_reader = csv.DictReader(f, delimiter=",")
        csv_writer = csv.DictWriter(f, fieldnames=csv_reader.fieldnames)
        row = {
            "": "AMC Javelin",
            "mpg": 15.2,
            "cyl": 8,
            "disp": 304,
            "hp": 150,
            "drat": 3.15,
            "wt": 3.435,
            "qsec": 17.3,
            "vs": 0,
            "am": 0,
            "gear": 3,
            "carb": 2,
        }

        csv_writer.writerow(row)


def main():
    # read_csv_cars()
    read_csv_as_dict()


if __name__ == "__main__":
    main()

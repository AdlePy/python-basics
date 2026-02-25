class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

    def copy(self):
        return Date(year=self.year, month=self.month, day=self.day)

    @classmethod
    def from_date_string(cls, date_string: str):
        year, month, day = map(int, date_string.split("-"))
        date = cls(year=year, month=month, day=day)
        return date

    @staticmethod
    def is_date_string_valid(date_string: str):
        if date_string.count("-") != 2:
            return False

        year, month, day = map(int, date_string.split("-"))

        return day <= 31 and month <= 12 and year <= 4000


my_date = Date(1996, 7, 21)
print(my_date)

processed_date = Date.from_date_string("2026-3-19")
print(processed_date)

print(Date.is_date_string_valid("2025-4-31"))

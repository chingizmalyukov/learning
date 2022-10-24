class Date:
    def __init__(self, day: int = 0, mouth: int = 0, year: int = 0) -> None:
        self.day = day
        self.mouth = mouth
        self.year = year

    def __str__(self) -> str:
        return 'День: {}\tМесяц {}\tГод {}'.format(
            self.day, self.mouth, self.year
        )

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        day, mouth, year = map(int, date.split('-'))
        return 0 < day <= 31 and 0 < mouth <= 12 and 0 < year <= 9999

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        day, mouth, year = map(int, date.split('-'))
        date_obj = cls(day, mouth, year)
        return date_obj


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

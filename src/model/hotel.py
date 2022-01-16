from enum import Enum


class DayType(Enum):
    WEEKDAY = 1
    WEEKEND = 2


class Hotel:
    def __init__(self, name: str, weekday_rate: float, weekend_rate: float) -> None:
        self.name = name
        self.weekday_rate = weekday_rate
        self.weekend_rate = weekend_rate

    def get_rate(self, day: DayType) -> float:
        if day == DayType.WEEKDAY:
            return self.weekday_rate
        else:
            return self.weekend_rate

from enum import Enum
from typing import NamedTuple


class DayType(Enum):
    WEEKDAY = 1
    WEEKEND = 2


class RateCard(NamedTuple):
    weekday: float
    weekend: float


class Hotel:
    def __init__(self, name: str, rate_card: RateCard) -> None:
        self.name = name
        self.rate_card = rate_card

    def get_rate(self, day: DayType) -> float:
        if day == DayType.WEEKDAY:
            return self.rate_card.weekday
        else:
            return self.rate_card.weekend

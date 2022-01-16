from src.model.hotel import Hotel, DayType, RateCard


class TestHotel:
    class TestRateCard:
        def test_get_rate_should_return_specified_weekday_rate(self):
            hotel = Hotel("X", RateCard(100, 120), 5)
            assert hotel.get_rate(DayType.WEEKDAY) == 100

        def test_get_rate_should_return_specified_weekend_rate(self):
            hotel = Hotel("X", RateCard(100, 120), 5)
            assert hotel.get_rate(DayType.WEEKEND) == 120

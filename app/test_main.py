import datetime
import pytest
from unittest.mock import patch
from app.main import outdated_products


@pytest.mark.parametrize(
    "today, input_data, expected",
    [
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 15),
                    "price": 160
                }
            ],
            []
        ),
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["duck"]
        ),
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 1, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 1, 20),
                    "price": 160
                }
            ],
            ["salmon", "chicken", "duck"]
        ),
        (
            datetime.date(2022, 2, 2),
            [],
            []
        )
    ]
)
def test_outdated_products(
        today: datetime.date,
        input_data: list,
        expected: list
) -> None:
    with (patch("app.main.datetime") as mock_datetime):
        mock_datetime.date.today.return_value = today
        mock_datetime.date.side_effect = lambda *args, **kwargs: datetime.date(
            *args,
            **kwargs
        )
        assert outdated_products(input_data) == expected

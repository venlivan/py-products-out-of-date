import datetime
import pytest
from unittest.mock import patch, MagicMock
from app.main import outdated_products


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
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
            [],
            []
        )
    ]
)
@patch("app.main.datetime.date.today", return_value=datetime.date(2022, 2, 2))
def test_outdated_products(
        mock_today: MagicMock,
        input_data: list,
        expected: list
) -> None:
    assert outdated_products(input_data) == expected

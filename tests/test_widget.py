import pytest

from src.widget import processing_inform_card_account, get_date

# Использование параметризации


@pytest.mark.parametrize("x, expected", [("Visa Gold 1234", "It's not corrected input"),
                                         ("Visa Gold 123456781234567812", "It's not corrected input"),
                                         ("Visa Gold 1234567812345678", "Visa Gold 1234 56** **** 5678"),
                                         ("Счет 123451234512345", "It's not corrected input"),
                                         ("Счет 123451234512345123456", "It's not corrected input"),
                                         ("Счет 12345123451234512345", "Счет **2345"),
                                         ("", "It's not corrected input")])
def test_processing_inform_card_account(x: str, expected: str) -> None:
    assert processing_inform_card_account(x) == expected


@pytest.mark.parametrize("y, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                                         ("2024-03-11T02:26:18.6714071", "It's not corrected input"),
                                         ("2024-03-T02:26:18.6714071", "It's not corrected input"),
                                         ("", "It's not corrected input")])
def test_get_date(y: str, expected: str) -> None:
    assert get_date(y) == expected

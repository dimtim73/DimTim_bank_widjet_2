import pytest

from src.masks import get_mask_card_number, get_mask_account


# Использование фикстур
@pytest.fixture
def all_number() -> list:
    return ['1234567812345678', '1234567812345679']


def test_get_mask_card_number(all_number: str) -> None:
    expected_results = ['1234 56** **** 5678', "1234 56** **** 5679"]  # Ожидаемые результаты для каждого элемента
    for number, expected in zip(all_number, expected_results):
        assert get_mask_card_number(number) == expected


def test_get_mask_account(all_number: str) -> None:
    expected_results = ['**5678', "**5679"]  # Ожидаемые результаты для каждого элемента
    for number, expected in zip(all_number, expected_results):
        assert get_mask_account(number) == expected

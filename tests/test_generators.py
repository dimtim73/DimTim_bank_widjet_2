import pytest


from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions_list


# Фикстура для тестов
@pytest.fixture
def transactions():
    """предоставляет список транзакций для всех тестов.
"""
    return transactions_list

# Тесты
def test_filter_by_currency(transactions):
    """проверяет правильность фильтрации по валюте"""
    result = filter_by_currency(transactions, 'USD')
    assert len(list(result)) == 5
    assert all(trans["operationAmount"]["currency"]["name"] == 'USD' for trans in result)

def test_transaction_descriptions(transactions):
    """проверяет правильность получения описаний транзакций"""
    result = transaction_descriptions(transactions)
    result_list = list(result)
    assert len(result_list) == 5
    assert 'Перевод организации' in result_list
    assert 'МАХинация' in result_list

@pytest.mark.parametrize("start, finish, expected", [
    (1, 4, ["0000 0000 0000 0001",
             "0000 0000 0000 0002",
             "0000 0000 0000 0003"]),
    (10, 13, ["0000 0000 0000 0010",
              "0000 0000 0000 0011",
              "0000 0000 0000 0012"]),
])
def test_card_number_generator(start, finish, expected):
    """параметризованный тест для проверки генерации номеров карт"""
    result = list(card_number_generator(start, finish))
    assert result == expected

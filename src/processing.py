def filter_by_state(list_vocab: list, state = 'EXECUTED') -> list:
    """Функция возвращает строку с замаскированным номером. Для карт и счетов используются разные типы маскировки."""
    filtered_list = []
    for vocab in list_vocab:
        if vocab['state'] == state:
            filtered_list.append(vocab)
    return filtered_list


def sort_by_date(list_vocab_filter: list, sort_way = True) -> list:
    """Функция  возвращает новый список словарей, отсортированный по дате (date)."""
    list_vocab_sort = sorted(list_vocab_filter, key=lambda x: x['date'], reverse=sort_way)
    return list_vocab_sort


print(sort_by_date(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])))
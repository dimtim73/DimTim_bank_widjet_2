def filter_by_state(list_vocab: list, state: str = 'EXECUTED') -> list:
    """Функция возвращает список словарей, отфильтрованных по ключу 'state'."""
    filtered_list = []
    for vocab in list_vocab:
        if vocab['state'] == state:
            filtered_list.append(vocab)
    return filtered_list


def sort_by_date(list_vocab_filter: list, sort_way: bool = True) -> list:
    """Функция возвращает новый список словарей, отсортированный по дате (date)."""
    try:
        list_vocab_sort = sorted(list_vocab_filter, key=lambda x: x['date'], reverse=sort_way)
    except Exception:
        temp_list = ["It's not corrected input"]
        return temp_list
    else:
        return list_vocab_sort

# print(filter_by_state([{'id': 939719570, 'state': 'EXECTED', 'date': '2018-06-30T02:08:58.425572'}]))
# print(sort_by_date(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])))

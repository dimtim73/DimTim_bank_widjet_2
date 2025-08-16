import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("x, expected",
                         [([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],
                           [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]),
                          ([{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],
                           [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                          ([{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}],
                           []),
                          ([{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                           []),
                          ([], [])])
def test_test_filter_by_state(x: list, expected: list) -> None:
    assert filter_by_state(x) == expected


@pytest.fixture
def date_test_base() -> list:
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 594226725, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_sort_by_date(date_test_base: list) -> None:
    sort_list_data = sort_by_date(date_test_base)
    len_sort_list_data = len(sort_list_data)
    for item in range(len_sort_list_data - 1):
        assert sort_list_data[item]['date'] >= sort_list_data[item + 1]['date']

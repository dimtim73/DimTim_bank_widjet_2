transactions_list = [
    {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       },
    {
              "id": 142264200,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       },
    {
          "id": 939719000,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "МАХинация",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142260000,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на карту",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       },]

def filter_by_currency (transactions: list, currency_list):
    """ Функция принимает на вход список словарей, представляющих транзакции."""

    transaction = [trans for trans in transactions if trans["operationAmount"]["currency"]["name"] == "USD"]
    return transaction


usd_transactions = filter_by_currency(transactions_list, "USD")
iterator = iter(usd_transactions)
for _ in range(2):
    print(next(iterator))


def transaction_descriptions(transactions: list):
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
"""
    descriptions = [transactions["description"] for transactions in transactions]
    return descriptions


descriptions_list = transaction_descriptions(transactions_list)
iterator = iter(descriptions_list)
for _ in range(5):
    print(next(iterator))


def card_number_generator(start, finish):
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    card_number_int = [str(x) for x in range(start, finish)]
    print(card_number_int)
    pattern = "0000000000000000"
    card_numbers = []
    for n in card_number_int:
        p = pattern[:-len(n)] + n
        p = p[:4] + " " + p[4:8] + " " + p[8:12] + " " + p[12:]
        yield p
        #card_numbers.append(p)

    return card_numbers


for card_number in card_number_generator(1, 11):
    print(card_number)

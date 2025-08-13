from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def processing_inform_card_account(card_account_information: str) -> str:
    """Функция принимает номер карты или счета и возвращает замаскированный номер"""
    list_information = card_account_information.split()

    pay_list = ["счет", "visa", "mastercard", "discover", "maestro", "UnionPay", "JCB", "jcb", "мир"]
    if len(list_information) == 0:
        return "It's not corrected input"
    else:

        a = list_information[0].lower() in pay_list
        b = list_information[-1].isdigit()
        c = len(list_information[-1]) == 16 or len(list_information[-1]) == 20
        d = len(list_information) == 2 or len(list_information) == 3
        if a and b and c and d:

            if list_information[0].lower() == "счет":
                mask_number = 'Счет ' + get_mask_account(list_information[-1])
                return mask_number
            else:
                if len(list_information) == 2:
                    mask_number = str(list_information[0]) + " " + get_mask_card_number(list_information[-1])
                    return mask_number
                else:
                    mask_number = str(list_information[0]) + " " + str(list_information[1]) + " " + \
                        get_mask_card_number(list_information[-1])
                    return mask_number
        else:
            return "It's not corrected input"


def get_date(date_str: str) -> str:
    """Функция возвращает строку в формате даты"""
    try:
        full_data = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    except Exception:
        return "It's not corrected input"
    else:
        return full_data.strftime("%d.%m.%Y")


# print(processing_inform_card_account("Visa Gold 5999414228426353"))
# print(processing_inform_card_account(""))
#
# print(get_date("2024-03-11T02:26:18.671407"))
# print(get_date("2024-03-112:26:18.671407"))

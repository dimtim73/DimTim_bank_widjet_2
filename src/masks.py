def get_mask_card_number(card_number: str)-> str:
    """ Функция маскировки номера банковской карты """

    card_number = str(card_number)
    card_number_mask = card_number[:4] + " " + card_number[4:6] + "** ****" + " " + card_number[12:]
    return card_number_mask


# print(get_mask_card_number(str(7000792289606361)))


def get_mask_account(account_number: str) -> str:
    """ Функция маскировки номера банковского счета """
    account_number = str(account_number)
    account_number_mask = "**" + account_number[-4:]
    return account_number_mask


# print(get_mask_account(str(73654108430135874305)))

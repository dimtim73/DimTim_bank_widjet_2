from src.masks import get_mask_account, get_mask_card_number


def processing_inform_card_account(card_account_information):
    list_information = card_account_information.split()
    pay_list= ["счет", "visa", "mastercard", "discover", "maestro", "UnionPay", "JCB", "jcb", "мир"]

    a = list_information[0].lower() in pay_list
    b = list_information[-1].isdigit()
    c = len(list_information[-1]) == 16 or len(list_information[-1]) == 20
    d = len(list_information) == 2 or len(list_information) == 3
    if a and b and c and d:

        if list_information[0].lower() == "счет":
            mask_number = 'Счет ' + get_mask_account(list_information[-1])
            print(mask_number)
        else:
            if len(list_information) == 2:
                mask_number = str(list_information[0]) + " " + get_mask_card_number(list_information[-1])
                print(mask_number)
            else:
                mask_number = str(list_information[0]) + " " + str(list_information[1]) + " " + get_mask_card_number(list_information[-1])
                print(mask_number)
    else:
        print("It's not corrected input")


processing_inform_card_account("Visa Gold 5999414228426353")
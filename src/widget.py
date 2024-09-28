def mask_account_card(info):
    '''Функция принимает информацию о карте и маскирует номер'''
    parts = info.split()
    card_type = ' '.join(parts[:-1])
    number = parts[-1]

    if 'Счет' in card_type:
        masked_number = f"{card_type} **{number[-4:]}"
    else:
        masked_number = f"{card_type} {number[:4]} {number[4:6]}** **** {number[-4:]}"

    return masked_number

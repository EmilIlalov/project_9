def mask_account_card(info):
    '''Функция принимает информацию о карте и маскирует номер'''
    # Объединяем инфо о карте в список
    parts = info.split()
    # Создаем строку без номера используя срез
    card_type = ' '.join(parts[:-1])
    # Создаем номер
    number = parts[-1]

    if 'Счет' in card_type:
        masked_number = f"{card_type} **{number[-4:]}"

    else:
        masked_number = f"{card_type} {number[:4]} {number[4:6]}** **** {number[-4:]}"

    return masked_number


def get_date(date_str):
    '''Функция принимает дату и возвращает в формате ДД.ММ.ГГГГ'''
    # Разделяем строку по символу 'T' в список
    date_part = date_str.split('T')[0]
    # Разделяем дату по символу '-'
    year, month, day = date_part.split('-')

    return f"{day}.{month}.{year}"

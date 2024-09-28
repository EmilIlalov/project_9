def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты и возвращает замаскированное значение"""
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр.")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(mask_account: str) -> str:
    """Функция принимает номер счета и возвращает замаскированную его часть"""
    if len(mask_account) != 20 or not mask_account.isdigit():
        raise ValueError("Номер счета должен содержать 20 цифр.")
    return f"**{mask_account[-4:]}"

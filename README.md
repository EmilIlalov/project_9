# Проект 9.1

## Описание:
Это виджет, который показывает несколько последних успешных банковских операций клиента.

## Установка:

* Клонируйте репозиторий:
```
git clone https://github.com/EmilIlalov/project_card
```

## Примеры кода и функционала:
* Функция в модуле  **masks** `get_mask_card_number` принимает на вход номер карты и возвращает ее маску:
```
def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты и возвращает замаскированное значение"""
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр.")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
```
* В модуле **widget** есть функция `mask_account_card` которая умеет обрабатывать информацию как о картах, так и о счетах:
```
def mask_account_card(info: str) -> str:
    """Функция принимает информацию о карте и маскирует номер"""
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
```
## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).

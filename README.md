# Проект 10_1

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
## Тестирование:
В директории `tests/` есть модули с тестированием всего функционала актуальной версии программы.
## Запуск тестов:
* Воспользуйтесь терминалом и введите:

`pytest tests/[имя_файла]`

Для тестирования вам потребуется зависимость, а именно библиотека **pytest**. Для установки откройте терминал:

### Установка через pip:

Чтобы установить **pytest**, выполните следующую команду в терминале:
```
python get-pip.py
pip install pytest
```

### Через **Poetry**:
```
poetry install
poetry shell
poetry add --dev pytest
```
* **shell** активирует виртуальное окружение.

* Флаг **--dev** указывает, что **pytest** является зависимостью для разработки.

## Генераторы:
Генераторы в Python — это удобный способ создания итераторов, которые позволяют генерировать последовательности значений по мере необходимости. 
Они экономят память и делают код более читаемым.

### Преимущества генераторов
- **Экономия памяти**: Генераторы не загружают все значения в память сразу.
- **Читаемость кода**: Код с генераторами часто проще и понятнее.

### Примеры использования:
Генераторы находятся в директории `src/generators.py`. Пример функции-генератора:
```
def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX
    Диапазоны передаются как параметры генератора."""
    for num in range(start, stop + 1):
        number = "0" * (16 - len(str(num))) + str(num)
        string_to_return = ""
        block_counter = 0
        for digit in number:
            block_counter += 1
            if block_counter <= 4:
                string_to_return += digit
            else:
                string_to_return += " " + digit
                block_counter = 1
        yield string_to_return

```

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).

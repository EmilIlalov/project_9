import os
from functools import wraps
from typing import Union

import pytest

from src.decorators import log


# Пример функции с декоратором
@log("test.log.txt")
def my_function(x: int, y: int) -> int:
    """Функция вызова декоратора с файлом сохранения test.log.txt"""
    return x + y


# Функция, которая вызывает ошибку
@log("test.log_error.txt")
def function_error(x: int, y: int) -> Union[int, float, None]:
    """Функция вызова декоратора с ошибкой и сохранения вывода в файл test.log_error.txt."""
    return x / y


# Тесты
@pytest.fixture
def test_log_file():
    @log(filename="mylog.txt")
    def example_function(x, y):
        return x * y

    result = example_function(5, 100)

    with open(os.path.join("logs", "mylog.txt"), "rt") as file:
        log_string = file.readline()  # Читаем только первую строку

    assert log_string == "example_function ok. Result: 500\n"
    assert result == 500


# Тест вывода в консоль при успешной работе функции.
def test_log_console(capsys):
    @log()
    def example_function(x, y):
        return x * y

    result = example_function(5, 100)

    captured = capsys.readouterr()

    assert captured.out == "example_function ok. Result: 500\n"
    assert result == 500


# Тест записи в файл, если произошла ошибка.
def test_log_file_raise():
    @log(filename="mylog.txt")
    def example_function(x, y):
        raise TypeError("Что-то пошло не так")

    with pytest.raises(TypeError, match="Что-то пошло не так"):
        example_function(5, 100)

    with open(os.path.join("logs", "mylog.txt"), "rt") as file:
        log_string = file.readline()  # Читаем только первую строку

    assert log_string == "example_function error: TypeError. Inputs: (5, 100), {}\n"


def test_log_decorator() -> None:
    result = my_function(2, 3)

    assert result == 5

    # Проверка лога
    with open("test.log.txt", "r") as file:
        log_contents = file.read()

    assert "my_function ok" in log_contents

    # Тестирование вызова функции с ошибкой
    with pytest.raises(ZeroDivisionError):
        function_error(2, 0)

    # Проверка лога ошибки
    with open("test.log_error.txt", "r") as file:
        log_contents = file.read()

    assert "function_error error" in log_contents

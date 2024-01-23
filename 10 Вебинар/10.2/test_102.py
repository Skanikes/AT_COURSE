# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def test01():
    assert all_division(20, 2, 2 ) == 5


def test_change_01():
    assert all_division(10, 2, 2) == 2.5


def test_change_02():
    assert all_division(15, 3, 2 ) == 2.5

@pytest.mark.smoke
def test04():
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0, 2 )

@pytest.mark.large
def test05():
    assert all_division(1000, 10, 2 ) == 50



def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division



















#pytest -v test_102.py
#pytest -m smoke -v test_102.py
#pytest -k change  -v test_102.py

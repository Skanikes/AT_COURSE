# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest

import pytest


def test01():
    assert all_division(20, 2, 2 ) == 5


def test_change_01():
    assert all_division(10, 2, 2) == 2.5


def test_change_02():
    assert all_division(15, 3, 2 ) == 2.5

@pytest.mark.parametrize("input_data, expected_output",
    [
    ((10, 2, 2), 2.5),        # Тест 1
    pytest.param((20, 4, 0), None, marks=pytest.mark.skip("Деление на ноль")),  #cкипываем
    ((100, 5, 2), 10),        # Тест 3
    ((8, 2, 2, 2), 1),        # Тест 4
    ((15, 3), 5),             # Тест 5
    ])


def test_all_division(input_data, expected_output):
    result = all_division(*input_data)
    assert result == expected_output

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
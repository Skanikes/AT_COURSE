# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.



class TestClass:

    def test_one(self, session_fixture, test_fixture):
        assert 1 == 1
        print("test1")

    def test_two(self, test_fixture):
        assert 2 == 2
        print("test2")

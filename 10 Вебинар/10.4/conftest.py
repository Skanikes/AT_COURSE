import pytest
import time


@pytest.fixture(scope="session")
def session_fixture():
    start_time = time.time()
    print(f"\n'Начало выполнения класса тестов'")

    yield

    end_time = time.time()
    print(f'\n Окончание выполнения класса тестов. Время выполнения: {end_time - start_time} сек.')


@pytest.fixture()
def test_fixture():
    start_time = time.time()
    print('Начало выполнения теста')

    yield

    end_time = time.time()
    print(f'Окончание выполнения теста. Время выполнения: {end_time - start_time} сек.')
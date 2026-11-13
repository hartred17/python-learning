from employee import Employee
import pytest


@pytest.fixture
def setUp():
    """Создает экземпляр Employee."""
    employee = Employee("ivan", "ivanov", 10_000)
    return employee


def test_give_default_raise(setUp):
    """Тестирует значение amount по умолчанию."""
    setUp.give_raise()
    assert setUp.sallary == 15_000


def test_give_custom_raise(setUp):
    """Тестирует кастомное значение amount."""
    setUp.give_raise(10_000)
    assert setUp.sallary == 20_000

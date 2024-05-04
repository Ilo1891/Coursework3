from src.utils import get_last_five_operations
import pytest as pytest


@pytest.fixture
def utils_fixture():
    return [{"id": "1", "date": "01.01.2023", "state": "EXECUTED"},
            {},
            {"id": "2", "date": "01.03.2023", "state": "EXECUTED"},
            {"id": "3", "date": "01.02.2023", "state": "EXECUTED"},
            {"id": "4", "date": "01.05.2023", "state": "CANCELED"},
            {"id": "5", "date": "01.04.2023", "state": "EXECUTED"},
            {"id": "6", "date": "01.06.2023", "state": "EXECUTED"}]


def test_get_last_five_operations(utils_fixture):
    assert get_last_five_operations(utils_fixture) == [{"id": "6", "date": "01.06.2023", "state": "EXECUTED"},
                                                       {"id": "5", "date": "01.04.2023", "state": "EXECUTED"},
                                                       {"id": "2", "date": "01.03.2023", "state": "EXECUTED"},
                                                       {"id": "3", "date": "01.02.2023", "state": "EXECUTED"},
                                                       {"id": "1", "date": "01.01.2023", "state": "EXECUTED"}]
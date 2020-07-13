import pytest
from app.calc import Calculator


@pytest.fixture()
def up_down():
    c = Calculator()
    print('start calculating')
    yield c
    print('\ncalculating finished')

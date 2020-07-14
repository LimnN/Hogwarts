import pytest
import yaml
import os
from app.calc import Calculator

current = os.path.dirname(__file__)
file = os.path.join(current, 'data/envs.yml')
envs = yaml.safe_load(open(file, 'r'))


@pytest.fixture()
def up_down():
    c = Calculator()
    print('start calculating')
    yield c
    print('\ncalculating finished')


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='test')


@pytest.fixture()
def env(request):
    cu_env = request.config.getoption('--env')
    try:
        return envs[cu_env]
    except KeyError as e:
        print(e)
        return envs['test']


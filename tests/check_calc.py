import pytest
import json
import os


path = os.path.dirname(__file__)
file = os.path.join(path, 'data/cases.json')
data = json.load(open(file, 'r'))
adds = data['add']
subs = data['sub']
muls = data['mul']
divs = data['div']


def check_env(env):
    myenv = env
    host = myenv['host']
    port = myenv['port']
    print('http://' + host + ':' + str(port))


class CheckCalc:
    @pytest.mark.parametrize('a, b, result', adds)
    @pytest.mark.dependency(name='add')
    @pytest.mark.run(order=1)
    def check_add(self, up_down, a, b, result):
        print('here is add')
        assert result == up_down.add(a, b)

    @pytest.mark.parametrize('a, b, result', subs)
    @pytest.mark.dependency(name='sub', depends=['add'])
    @pytest.mark.run(order=2)
    def check_sub(self, up_down, a, b, result):
        print('here is sub')
        assert result == up_down.sub(a, b)

    @pytest.mark.parametrize('a, b, result', muls)
    @pytest.mark.dependency(name='mul')
    @pytest.mark.run(order=3)
    def check_mul(self, up_down, a, b, result):
        print('here is mul')
        assert result == up_down.mul(a, b)

    @pytest.mark.parametrize('a, b, result', divs)
    @pytest.mark.dependency(name='div', depends=['mul'])
    @pytest.mark.run(order=4)
    def check_div(self, up_down, a, b, result):
        print('here is div')
        assert result == up_down.div(a, b)

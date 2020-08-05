from app import calc
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


class TestCalc:
    @pytest.mark.parametrize('a, b, result', adds)
    def test_add(self, up_down, a, b, result):
        assert result == up_down.add(a, b)

    @pytest.mark.parametrize('a, b, result', subs)
    def test_sub(self, up_down, a, b, result):
        assert result == up_down.sub(a, b)

    @pytest.mark.parametrize('a, b, result', muls)
    def test_mul(self, up_down, a, b, result):
        assert result == up_down.mul(a, b)

    @pytest.mark.parametrize('a, b, result', divs)
    def test_div(self, up_down, a, b, result):
        assert result == up_down.div(a, b)


if __name__ == '__main__':
    pytest.main(["-s", "--alluredir", "./report/result"])

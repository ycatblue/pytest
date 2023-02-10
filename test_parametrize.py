import pytest

'''
list_one = [1, 2, 3, 4]


@pytest.mark.parametrize('number', list_one)
def test_parametrize(number):
    assert number in list_one

'''

list_two = [(1, 2, 3), (2, 3, 5), (5, 6, 7)]


@pytest.mark.parametrize('num1, num2, sum', list_two)
def test_parametrize2(num1, num2, sum):
    assert num1 + num2 == sum

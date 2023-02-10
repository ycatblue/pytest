import pytest


def add_number(a, b):
    return a + b


@pytest.mark.done()
def test_add1():
    assert add_number(3, 2) == 5


@pytest.mark.undo
def test_add2():
    assert add_number(1, 1) == 3


@pytest.mark.undo
def test_add3():
    assert add_number(2, 2) == 5

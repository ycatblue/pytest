import pytest


@pytest.mark.xfail(reason="operation error")
def test_xfail1():
    assert 1 + 1 == 1


@pytest.mark.xfail
def test_xfail2():
    assert 1 + 1 == 2


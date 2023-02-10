import pytest


@pytest.mark.skip()
def test_skin1():
    assert 1 == 2


@pytest.mark.skip(reason="skin this case")
def test_skin2():
    assert 1 == 2

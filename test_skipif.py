import pytest


@pytest.mark.skipif('sys.platform == "win32"', reason="It not allow run by win32")
def test_skipif1():
    assert 1 == 2


@pytest.mark.skipif('sys.platform != "win32"')
def test_skipif2():
    assert 1 == 1

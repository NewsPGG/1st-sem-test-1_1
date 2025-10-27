from src.fast_pow import fastPow


def test_two_power_two():
    assert fastPow(2, 2) == 4


def test_negative():
    assert fastPow(-1, 4) == 1

def test_negative_pow():
    assert fastPow(3, -2) == 1/9

def test_zero_pow():
    assert fastPow(100, 0) == 1

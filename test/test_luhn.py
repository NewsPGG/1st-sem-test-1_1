from src.luhn import luhnСheck


def test_good():
    assert luhnСheck("8571 2612 1234 5427")


def test_bad():
    assert not luhnСheck("4561 2612 1234 5463")

def test_good_even_positions_numbers():
    assert luhnСheck("9191 9191 9191 9194")

def test_bad_even_positions_numbers():
    assert not luhnСheck("9191 9191 9191 9191")

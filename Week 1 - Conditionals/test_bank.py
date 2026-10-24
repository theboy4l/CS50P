from bank import value


def test_startwith_h():
    assert value("hie how are you") == 20


def test_no_h():
    assert value("Good morning") == 100


def test_hello():
    assert value("hello Munya") == 0


def test_uppercase():
    assert value("HELLO Munya") == 0

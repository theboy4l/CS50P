from plates import is_valid


def test_numbers_at_the_end():
    assert is_valid("AAA123") is True
    assert is_valid("AAA12A") is False
    assert is_valid("A1B2C3") is False


def test_first_number_zero():
    assert is_valid("AAA01") is False
    assert is_valid("CS05") is False
    assert is_valid("AAA10") is True


def test_only_letters():
    assert is_valid("AAAAAA") is True
    assert is_valid("ABC") is True


def test_length():
    assert is_valid("CS50PM345638F") is False


def test_alpha_beginning():
    assert is_valid("AAA123") is True


def test_alpha_numeric():
    assert is_valid("AAA123") is True


def test_punctuation():
    assert is_valid("PI3.14") is False
    assert is_valid("AA 12") is False

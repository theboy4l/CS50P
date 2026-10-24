from numb3rs import validate


def test_ipv4_inrange():
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True


def test_ipv4_notrange():
    assert validate("512.512.512.512") is False
    assert validate("1.2.3.1000") is False


def test_leading_zeros():
    assert validate("192.168.001.1") is False


def test_letters():
    assert validate("cat") is False

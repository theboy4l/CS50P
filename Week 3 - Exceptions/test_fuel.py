from fuel import convert, gauge
import pytest


def test_x_greater():
    with pytest.raises(ValueError):
        convert("4/3")


def test_negatives():
    with pytest.raises(ValueError):
        convert("-1/3")


def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")


def test_percentage_less_or_equal_one():
    assert gauge(1) == "E"
    assert gauge(0) == "E"


def test_percentage_greater_or_equal_ninetynine():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_percentage():
    assert gauge(67) == "67%"


def test_non_int():
    with pytest.raises(ValueError):
        convert("abc")

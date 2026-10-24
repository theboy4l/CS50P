from seasons import convert_to_minutes, get_input, days_difference
import pytest
from datetime import date, timedelta


def test_correct_result():
    assert convert_to_minutes(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_to_minutes(366) == "Five hundred twenty-seven thousand forty minutes"
    assert convert_to_minutes(730) == "One million, fifty-one thousand, two hundred minutes"
    assert convert_to_minutes(731) == "One million, fifty-two thousand, six hundred forty minutes"


def test_date_format():
    with pytest.raises(SystemExit):
        get_input("not-a-date")
    with pytest.raises(SystemExit):
        get_input("2026-13-01")


def test_days():
    assert days_difference(date.today() - timedelta(days=1)) == 1
    assert days_difference(date.today() - timedelta(days=2)) == 2

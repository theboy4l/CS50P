from datetime import date
import sys
import inflect


def main():
    d = input("Date of birth: ").strip()
    d = get_input(d)
    d = days_difference(d)
    print(convert_to_minutes(d))


def get_input(d):
    try:
        year, month, day = d.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        return date(year, month, day)
    except ValueError:
        sys.exit("Invalid")


def days_difference(dob):
    current_date = date.today()
    delta_days = current_date - dob
    return delta_days.days


def convert_to_minutes(days):
    minutes = days * 24 * 60
    p = inflect.engine()
    result = p.number_to_words(minutes, andword="")
    return f"{result.capitalize()} minutes"


if __name__ == "__main__":
    main()

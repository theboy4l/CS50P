def main():
    time = convert(input("what time is it: ").strip())
    meals = meal(time)
    if meals:
        print(meals)


def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + float(minutes) / 60


def meal(time):
    if 7.0 <= time <= 8.0:
        return "breakfast time"
    elif 12.0 <= time <= 13.0:
        return "lunch time"
    elif 18.0 <= time <= 19.0:
        return "dinner time"


if __name__ == "__main__":
    main()

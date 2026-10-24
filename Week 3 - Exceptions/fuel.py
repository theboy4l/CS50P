def main():
    while True:
        try:
            fraction = input("Enter to check fuel in the form (x/y): ")
            percentage = convert(fraction)
            break
        except ZeroDivisionError:
            print("Y can not be zero")
        except ValueError:
            print("insert the right values")

    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    if x < 0:
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

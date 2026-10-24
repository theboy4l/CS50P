def main():
    dollars = dollars_to_float(input("How much is the meal: "))
    percentage = percentage_to_float(input("How much is the tip: "))
    tip = dollars * percentage
    print(f"leave {tip:.2f}")


def dollars_to_float(d):
    new_val = d.lstrip("$")
    return float(new_val)


def percentage_to_float(p):
    new_val = p.rstrip("%")
    return float(new_val) / 100


main()

def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    orders(menu)


def orders(menu):
    total_cost = 0
    while True:
        try:
            order = input("Item: ").strip().title()
            total_cost = total_cost + menu[order]
            print("Total: $" + f"{total_cost:.2f}")
        except KeyError:
            pass
        except EOFError:
            print()
            break


main()

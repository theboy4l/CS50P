def main():
    items_list = []
    items_choice = {}

    while True:
        try:
            userinput = input().strip().lower()
            items_list.append(userinput)
            items_choice = {item.upper(): items_list.count(item) for item in items_list}
        except EOFError:
            print()
            break

    for item in sorted(items_choice.keys()):
        print(f"{items_choice[item]} {item}")


if __name__ == "__main__":
    main()

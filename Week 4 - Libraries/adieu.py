def main():
    goodbye()


def goodbye():
    user_list = userInput()

    if not user_list:
        return

    if len(user_list) > 2:
        pre_string = ", ".join(user_list[:-1])
        print(f"Adieu, adieu, to {pre_string}, and {user_list[-1]}")
    elif len(user_list) == 2:
        print(f"Adieu, adieu, to {' and '.join(user_list)}")
    else:
        print(f"Adieu, adieu, to {user_list[0]}")


def userInput():
    nameslist = []

    while True:
        try:
            user_Input = input("Name: ").strip()
            if user_Input:
                nameslist.append(user_Input)
        except EOFError:
            print()
            return nameslist


if __name__ == "__main__":
    main()

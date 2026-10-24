import emoji


def main():
    emojized_str = emojise()
    print(emojized_str)


def emojise():
    user_input = get_input()
    return emoji.emojize(user_input, language="alias")


def get_input():
    return input("Enter a string in English: ")


main()

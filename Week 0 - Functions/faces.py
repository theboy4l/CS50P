def main():
    user_input = input("say anything: ")
    print(convert(user_input))


def convert(text):
    text = text.replace(":(", "🙁")
    text = text.replace(":)", "🙂")
    return text


main()

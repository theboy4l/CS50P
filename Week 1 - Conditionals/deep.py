def main():
    user_input = input("what's the answer to the great question of life: ").lower().strip()
    if question_of_life(user_input):
        print("Yes")
    else:
        print("No")


def question_of_life(question):
    return question in ("42", "forty-two", "forty two")


main()

import random


def main():
    randomise()


def randomise():
    level = getlevel()
    rand_int = random.randint(1, level)
    while True:
        user_choice = get_int()
        if user_choice == rand_int:
            print("Just right!")
            break
        elif user_choice < rand_int:
            print("Too small!")
        else:
            print("Too large!")


def getlevel():
    while True:
        try:
            user_input = int(input("Level: ").strip())
            if user_input < 1:
                raise ValueError
        except ValueError:
            pass
        else:
            return user_input


def get_int():
    while True:
        try:
            user_input = int(input("Guess: ").strip())
            if user_input < 1:
                raise ValueError
        except ValueError:
            pass
        else:
            return user_input


if __name__ == "__main__":
    main()

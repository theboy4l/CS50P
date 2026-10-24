import random


def main():
    generate_integer()


def get_level():
    while True:
        user_input = input("Level: ").strip()
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input in [1, 2, 3]:
                return user_input


def generate_integer():
    level = get_level()
    score = 0
    questions = 0

    while questions < 10:
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        actual_answer = x + y
        tries = 0

        while tries < 3:
            try:
                user_answer = input(f"{x} + {y} = ")
                if int(user_answer) == actual_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"{x} + {y} = {actual_answer}")

        questions += 1

    print(f"Score: {score}")


if __name__ == "__main__":
    main()

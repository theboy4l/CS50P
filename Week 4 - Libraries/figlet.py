from pyfiglet import Figlet
import random
import sys


def main():
    render_text()


def render_text():
    user_input = get_input()
    figlet = Figlet()

    if user_input:
        figlet.setFont(font=user_input)
    else:
        choice = random.choice(figlet.getFonts())
        figlet.setFont(font=choice)

    text_to_render = input("Input: ")
    print(figlet.renderText(text_to_render))


def get_input():
    figlet = Figlet()

    if len(sys.argv) == 1:
        return None
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        userinput = sys.argv[2]
        if userinput in figlet.getFonts():
            return userinput
        else:
            sys.exit("Invalid font")
    else:
        sys.exit("Invalid usage")


main()

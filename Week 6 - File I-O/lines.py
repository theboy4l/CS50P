import sys


def main():
    filename = get_input()
    lines = count_lines(filename)
    print(lines)


def get_input():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".py"):
            return sys.argv[1]
        sys.exit("Not a Python file")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


def count_lines(filename):
    count = 0

    try:
        with open(filename, "r") as file:
            for line in file:
                stripped = line.lstrip()
                if stripped == "":
                    continue
                if stripped.startswith("#"):
                    continue
                count += 1
        return count
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

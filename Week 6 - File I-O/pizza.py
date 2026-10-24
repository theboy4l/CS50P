import csv
import sys
from tabulate import tabulate


def main():
    filename = get_input()
    print_table(filename)


def get_input():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
            return sys.argv[1]
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


def print_table(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            print(tabulate(reader, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

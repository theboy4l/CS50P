import sys
import csv


def print_table(r_filename, w_filename):
    try:
        with open(r_filename, "r") as infile:
            with open(w_filename, "w", newline="") as outfile:
                reader = csv.DictReader(infile)
                writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
                writer.writeheader()

                for line in reader:
                    last, first = line["name"].split(",")
                    last = last.strip()
                    first = first.strip()
                    house = line["house"].strip()
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {r_filename}")


def get_input():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    return sys.argv[1], sys.argv[2]


def main():
    r_filename, w_filename = get_input()
    print_table(r_filename, w_filename)


if __name__ == "__main__":
    main()

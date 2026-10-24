import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$"
    match = re.search(pattern, ip)
    is_valid = False

    if match:
        parts = [match.group(1), match.group(2), match.group(3), match.group(4)]
        firstpart = int(match.group(1))
        secondpart = int(match.group(2))
        thirdpart = int(match.group(3))
        lastpart = int(match.group(4))

        if (0 <= firstpart <= 255) and (0 <= secondpart <= 255) and (0 <= thirdpart <= 255) and (0 <= lastpart <= 255):
            is_valid = True

        for part in parts:
            if len(part) > 1 and part.startswith("0"):
                is_valid = False

    return is_valid


if __name__ == "__main__":
    main()

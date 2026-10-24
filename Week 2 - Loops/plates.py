def main():
    userinput = input("insert your number plate: ").upper()

    if is_valid(userinput):
        print("its valid")
    else:
        print("not valid")


def is_valid(plate):
    if not (2 <= len(plate) <= 6):
        return False

    if not plate.isalnum():
        return False

    if not plate[0:2].isalpha():
        return False

    seen = False

    for ch in plate:
        if ch.isdigit():
            if not seen and ch == "0":
                return False
            seen = True
        elif seen:
            return False

    return True


if __name__ == "__main__":
    main()

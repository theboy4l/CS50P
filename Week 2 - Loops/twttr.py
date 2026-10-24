def main():
    print(shorten("WHATS MY NAME"))


def shorten(word):
    new_word = ""
    for ch in word:
        if ch not in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            new_word += ch
    return new_word


if __name__ == "__main__":
    main()

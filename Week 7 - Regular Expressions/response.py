from validator_collection import validators, errors


def main():
    user_email = input("what's your email address: ").strip()
    print(validate_email(user_email))


def validate_email(email):
    try:
        validators.email(email)
        return "Valid"
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"


main()

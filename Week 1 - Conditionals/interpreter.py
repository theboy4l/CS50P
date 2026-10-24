def main():
    x, y, z = input("enter expression: ").strip().split()
    x = int(x)
    z = int(z)
    calculate(x, y, z)


def calculate(x, y, z):
    if y == "+":
        print(f"{x + z:.1f}")
    elif y == "-":
        print(f"{x - z:.1f}")
    elif y == "*":
        print(f"{x * z:.1f}")
    elif y == "/":
        print(f"{x / z:.1f}")


main()

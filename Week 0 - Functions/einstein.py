def main():
    user_mass = int(input("input m: "))
    energy = calc_joules(user_mass)
    print(energy)


def calc_joules(mass):
    return mass * (300000000**2)


main()

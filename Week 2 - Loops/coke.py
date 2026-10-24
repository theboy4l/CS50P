amount_due = 50

while amount_due > 0:
    print("Amount Due: " + str(amount_due))
    user_input = input("Insert Coin: ").strip()
    if user_input.isdigit():
        insert_coin = int(user_input)
    else:
        insert_coin = 0

    if insert_coin not in [25, 10, 5]:
        insert_coin = 0

    amount_due -= insert_coin

if amount_due <= 0:
    change_owed = 0 - amount_due
    print("Change Owed: " + str(change_owed))

user_input = input("write any sentence: ").strip()
output = ""

for ch in user_input:
    if ch == " ":
        output += "..."
    else:
        output += ch

print(output)

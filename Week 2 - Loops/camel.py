userinput = input("enter variable name: ")
emptystring = ""

for ch in userinput:
    if ch == ch.upper():
        emptystring = emptystring + "_" + ch.lower()
    else:
        emptystring = emptystring + ch

print(emptystring)

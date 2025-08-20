def parseNumber(answer, string):
    negative = False
    i = 0
    if string[0] == "-":
        negative = True
    for char in string:
        i += 1
        if negative == True and i == 1:
            continue
        if char not in "0123456789":
            return  [int(string[:i]), string[i:].strip()]

def parseOperation(answer, string):
    addition, subtract = False, False
    i = 0
    if string[0] == "+":
        addition = True
    elif string[0] == "-":
        subtract = True
    for char in string:
        i += 1
        if negative == True and i == 1:
            continue
        if char not in "0123456789":
            return  [int(string[:i]), string[i:].strip()]


# Expr = Number (("+" | "-") Number)*
# Term = Number
# Number = [0-9]+

print("Hesap Makinesi")
expr = input("\nLütfen işlemi giriniz:")
    
number = parseNumber(0, expr)
print(number[0] + 1)
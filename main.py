def parseNumber(string):
    negative = False
    i = 0
    if string[0] == "-":
        negative = True
    for char in string:
        i += 1
        if negative == True and i == 1:
            continue
        if char not in "0123456789":
            break
    if string[i:].strip() != '':
        return parseOperation(string[i:].strip())+int(string[:i])
    return int(string[:i])

def parseOperation( string):
    if string[0] == "+":
        return parseNumber(string[1:].strip())
    elif string[0] == "-":
        return parseNumber(string[1:].strip())*-1

print("Hesap Makinesi")
expr = input("\nLütfen işlemi giriniz:")
    
number = parseNumber(expr)
print(number)
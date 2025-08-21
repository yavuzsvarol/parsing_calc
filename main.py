def parseNumber(string):
    if not string:
        return "Hatalı girdi: Boş işlem"
    negative = False
    i = 0
    if string[0] == "-":
        negative = True
    for char in string:
        i += 1
        if negative == True and i == 1:
            continue
        if char not in "0123456789":
            i -= 1
            break
    try:
        if string[i:].strip() != '':
            return parseOperation(string[i:].strip())+int(string[:i])
        return int(string[:i])
    except:
        return "Hatalı girdi."

def parseOperation(string):
    if not string:
        return "Hatalı girdi: Boş işlem"
    if string[0] == "+":
        return parseNumber(string[1:].strip())
    elif string[0] == "-":
        return parseNumber(string[1:].strip())*-1

while True:
    print("\nHesap Makinesi")
    expr = input("Lütfen işlemi giriniz: ") 
    print("\nCevap: ", parseNumber(expr))
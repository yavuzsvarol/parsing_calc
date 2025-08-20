def parseNumber(number, string):
    negative = False
    i = 0
    if string[0] == "-":
        negative = True
    for char in string:
        i += 1
        if char not in "-0123456789":
            if negative == True: return [-1*int(string[1:i]), string[i:].strip()]
            return  [int(string[:i]), string[i:].strip()]
    

print("Hesap Makinesi")
expr = input("\nLütfen işlemi giriniz:")
    
number = parseNumber(0, expr)
print(number[0] + 1)
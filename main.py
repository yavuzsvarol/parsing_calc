class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i] == ' ':
            i += 1
            continue
        if expr[i] in '+-':
            k = i - 1
            while k >= 0 and expr[k] == ' ':
                k -= 1
            if k < 0 or expr[k] in '+-*/(':
                j = i + 1
                while j < len(expr) and expr[j].isdigit():
                    j += 1
                tokens.append(expr[i:j])
                i = j
                continue
            else:
                tokens.append(expr[i])
        elif expr[i].isdigit():
            j = i
            while j < len(expr) and expr[j].isdigit():
                j += 1
            tokens.append(expr[i:j])
            i = j
            continue
        i += 1
    return tokens

while True:
    print("\nHesap Makinesi")
    expr = input("Lütfen işlemi giriniz: ") 

    if not expr:
        print("Hatalı girdi: Boş işlem")
        continue
    tokens = tokenize(expr)

    for token in tokens:

        pass
        



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
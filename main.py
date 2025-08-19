class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def parseNumber(string):
    if string[0] == "-":
        negative = True
    i = 0
    for a in string:
        i += 1
        if a not in "0123456789":
            if negative == True: return [-1*int(string[:i]), string[i:]]
            return  [int(string[:i]), string[i:]]
    
print("Hesap Makinesi")
input = input("\nLütfen işlemi giriniz:")

        
number = parseNumber(input)
print(number[0] + 1)
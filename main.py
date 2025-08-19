class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def parseNumber(string):
    negative = False
    if string[0] == "-": negative = True
    i = 0
    for char in string:
        i += 1
        if char not in "0123456789":
            if string[:i] is "": return print("Beklenemeyen girdi.")
            if negative == True: return [-1*int(string[:i]), string[i:]]
            return  [int(string[:i]), string[i:]]
    
print("Hesap Makinesi")
input = input("\nLütfen işlemi giriniz:")

        
number = parseNumber(input)
print(number[0] + 1)
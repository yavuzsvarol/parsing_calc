class Tree:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

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

def tree_traverse(root):
    if root.left != None:
        tree_traverse(root.left)
    if root.left == None:
        return
    if root.data == "+":
        root.data = root.left.data + root.right.data
    elif root.data == "-":
        root.data = root.left.data - root.right.data
    return root.data

while True:
    print("\nHesap Makinesi")
    expr = input("Lütfen işlemi giriniz: ") 
    if not expr:
        print("Hatalı girdi: Boş işlem")
        continue
    tokens = tokenize(expr)
    for i in range(1, len(tokens), 2):
        if i == 1:
            root = Tree(int(tokens[i-1]))
        current = Tree(tokens[i])
        right = Tree(int(tokens[i+1]))
        current.left = root
        current.right = right
        root = current

    print("Sonuç: ", tree_traverse(root))

def forpyramide(grote): #forloop pyramide
    for i in range(grote + 1):
        print(i*'*')

    for i in reversed(range(grote)):
        print(i*'*')

def whilepyramide(grote): #whileloop pyramide
    i = 0
    while i < grote:
        i += 1
        print(i*'*')

    j = grote
    while j > 0:
        j -= 1
        print(j * '*')

def forrevpyramide(grote): #forloop reversed pyramid
    for i in range(grote + 1):
        print((grote - i) * ' '+ i*'*')

    for i in reversed(range(grote)):
        print(((grote - i) * ' ') + i * '*')

def whilerevpyramide(grote): #whileloop reversed pyramid
    i = 0
    while i < grote:
        i += 1
        print(((grote - i) * ' ') + i * '*')

    j = grote
    while j > 0:
        j -= 1
        print(((grote - j) * ' ') + j * '*')

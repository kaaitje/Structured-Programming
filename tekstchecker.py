def textchecker():
    string1 = input('geef een string:')
    string2 = input('geef nog een string:')
    c = 0
    while string1[c] == string2[c]:
        c += 1
    return ('Het eerste verschil zit op index '+ str(c))
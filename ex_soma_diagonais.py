'''
1. dado a matriz, calcular a soma das diagonais
matriz = [
    [1,3,6].
    [6,5,7],
    [6,9,11]
]
exemplo = 1+5+9+3+5+7
'''

matris = [
    [1,3,6],
    [6,5,7],
    [6,9,11]
]

a = 0
b = 0
cont = 0

for mtz in matris:
    a += mtz[cont]
    b += mtz[-(cont+1)]
    cont += 1

print (a + b)

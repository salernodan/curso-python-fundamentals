#!/usr/bin/python3
'''
1. dado a matriz , calcular a soma das diagonais
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
exemplo= 1+5+9+3+5+7
'''

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# a = 0
# b = 0
# cont = 0

# for mtz in matriz:
#     a += mtz[cont]
#     b += mtz[-(cont+1)]
#     cont += 1

# print (a + b)

# Usando enumerate
a = 0
b = 0

for cont, mtz in enumerate(matriz):
    a += mtz[cont]
    b += mtz[-(cont+1)]

print (a + b)


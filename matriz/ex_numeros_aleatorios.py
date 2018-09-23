#!/usr/bin/python3
from random import randint
from pprint import pprint
'''
1. Criar matriz com nr aleatorios e calcular a soma das diagonais
matriz = [
    [5,9,3],
    [1,4,6],
    [7,8,9]
]
exemplo= 1+5+9+3+5+7
'''
# Gerando uma matris com numeros aleatorios
matriz = [
    [randint(0,10) for x in range(3)],
    [randint(0,10) for x in range(3)],
    [randint(0,10) for x in range(3)]
]

# Calculando a soma das diagonais
soma = 0
for cont,x in enumerate(matriz):
    soma += x[cont]
    soma += x[-(cont+1)]

# Resultado
pprint(matriz)
print(soma)
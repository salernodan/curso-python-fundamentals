#!/usr/bin/python3

# Usando For com
# par = []

# for x in range(0, 100, 2):
#     par.append(x)

# List compretion com if ternario
numeros = [2, 4, 42343, 4342432, 2331, 10] 

par = [x for x in numeros if x % 2 == 0]

print(par)

# Usando for com if
# lista = []
# numeros = [2, 4, 42343, 4342432, 2331, 10]

# for x in numeros:
#     if x % 2 == 0:
#         lista.append(x)

# print(lista)        
        
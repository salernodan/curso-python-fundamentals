#!/usr/bin/python3

# List Comprehension com if ternario
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
        
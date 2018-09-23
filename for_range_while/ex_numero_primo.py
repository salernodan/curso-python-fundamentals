#!/usr/bin/python3

numero = int(input("Digite um numero para verificacao: "))

cont = 0

for x in range(1, numero + 1):
    if numero % x == 0:
        cont += 1

if cont > 2:
    print("Nao e primo")
else:
    print("primo")
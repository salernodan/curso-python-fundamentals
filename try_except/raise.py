#!/usr/bin/python3

ling = input("Qual a melhor linguagem de programacao: ")

try:
    if ling.lower().strip() == "python":
        print("Voce Acertou")
    else:
        raise ValueError("Linguagem errada!")
except ValueError as e:
    print('Erro: {}'.format(e))
#!/usr/bin/python3

'''Fazer uma funcao que retorna a quantidade de linhas de um arquivo'''

def contar_linhas(arquivo):
    with open(arquivo, "r") as arq:
        return len(arq.readlines())

cont = contar_linhas("nomes.txt")
print(cont)
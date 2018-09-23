#!/usr/bin/python3

def numerar_arq(nome):
    with open(nome, 'r') as arquivo:
        conteudo = arquivo.readlines()

    with open(nome, 'w') as arquivo:
        for cont ,x in enumerate(conteudo):
            arquivo.write('{}- {}'.format(cont +1, x))

numerar_arq('frutas.txt')

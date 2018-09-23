#!/usr/bin/python3

nomes = ['daniel', 'pedro', 'julia']

try:
    index = int(input("Digite um index para encontrar o convidado na lista: "))
    print(nomes[index])
except IndexError as ie:
    print("Nao foi encontrado o convidado na lista.\nErro: {}.".format(ie))


#!/usr/bin/python3

nomes = ['daniel', 'maria', 'joao']

busca = input('Digite um nome: ')

for nome in nomes:
    if nome == busca.strip().lower():
        print('achei')
        break
else:
    print('Nao achei')
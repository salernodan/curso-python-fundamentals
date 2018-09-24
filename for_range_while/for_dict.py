#!/usr/bin/python3

pessoas = [
    {'nome': 'daniel', 'idade': 24},
    {'nome': 'rafael', 'idade': 6},
    {'nome': 'renata', 'idade': 23},
    {'nome': 'yasmin', 'idade': 4},

]

for pessoa in pessoas:
    nome = pessoa['nome']
    idade = pessoa['idade']
print("O(A) {} tem {} anos".format(nome, idade))
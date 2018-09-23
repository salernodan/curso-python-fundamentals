#!/usr/bin/python3

# Exibe letras de A a Z
letras = []
for x in range(97, 97+26):
    letras.append(chr(x))
print(letras)

# List Comprehension
letras = [chr(x) for x in range(97, 97+26)]
print(letras)

# notas = int(input('Digite a quantidade de notas: '))
# soma = 0
# for x in range(notas):
#     nota = int(input('Digite a nota {0}: '.format(x+1)))
#     soma += nota
# media = soma / notas
# print('Media: {0}'.format(media))

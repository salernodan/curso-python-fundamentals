#!/usr/bin/python3

# Recebendo entrada do usuario
nota1 = int(input('Digite a nota 1: '))
nota2 = int(input('Digite a nota 2: '))

# Calcula media
media = (nota1 + nota2) / 2

# Saida
if media >= 7:
    print('Media: {0} \nAprovado'.format(media))
elif media > 3 and media < 7:
    print('Media: {0} \nRecuperacao'.format(media))
else:
    print('Media: {0} \nReprovado'.format(media))

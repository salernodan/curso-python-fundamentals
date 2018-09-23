#!/usr/bin/python3
'''
Faça um programa que leia algumas notas
e calcule a media,
notas maiores ou igual a 7 aprovado
maior que 3 e menor que 7 recuperação
menores ou igual a 3 reprovado
'''
try:
    qtd = int(input('Quantindade de notas: '))
except ValueError as e:
    print(e)
    print("Digite somente numeros")
    exit()
except Exception:
    pass


soma = 0
for x in range(qtd):
    try:
        nota = int(input('Digite nota{}: '.format(x+1)))
    except Exception:
        print("Digite somente numeros")
        exit()
    finally:
        print("Estou sempre aqui")    3
    if nota > 10:
        print('Nota invalida!')
        qtd -= 1
        continue
    soma += nota

media = soma / qtd

if media >= 7:
    print('Media {} , Aprovado'.format(media))
elif media > 3:
    print('Media {} , Recuperação'.format(media))
else:
    print('Media {} , Reprovado'.format(media))

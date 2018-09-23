#!/usr/bin/python3

convidados = ['daniel', 'maria', 'joao']
try: 
    pos = int(input('Digite posição do convidado: '))
    print(convidados[pos -1])
except ValueError:
    print('só é valido numeros')
except IndexError:
    print('a lista tem {} convidados'.format(len(convidados)))
except Exception as e:
    print("ERRO: {}".format(e))
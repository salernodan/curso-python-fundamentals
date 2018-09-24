#!/usr/bin/python3
# Scrip Python para automação de tarefas:
# Funcionalidade Criar arquivo adicionando shebang
# e dando permisão de execucao ./

from subprocess import run

name_arquivo = input('Digite o nome do arquivo: ')
try:
    with open(name_arquivo, 'r') as arquivo:
        conteudo = arquivo.readlines()
        conteudo.insert(0, '#!/usr/bin/python3\n')
    with open(name_arquivo, 'w+') as arquivo:
        for x in conteudo:
            arquivo.write(x)

except FileNotFoundError:
    with open(name_arquivo, 'a') as arquivo:
        arquivo.write('#!/usr/bin/python3\n')

run(['sudo', 'chmod', '+x', name_arquivo])
#!/usr/bin/python3
nomes = ['daniel', 'pedro', 'maria', 'renata']
nomes[0] = 'joao'

nomes.append('Rick')

nomes.insert(0, 'patrão')

for nome in nomes:
    print("Seja bem vindo {}".format(nome.title()))

while len(nomes) > 0:
    print(nomes)
    nomes.pop()

print(nomes)


# with open('frutas.txt', 'r') as arquivo:
#     conteudo = arquivo.readlines()
#     aux = []
#     for x in conteudo:
#         x = x.replace('\n', '')
#         aux.append(x)
#     # print(conteudo)
# print(aux)
# aux.insert(2, 'pessego')
# with open('frutas2.txt', 'w') as arquivo:
#     for item in aux:
#         arquivo.write('Fruta: {}\n'.format(item.title()))
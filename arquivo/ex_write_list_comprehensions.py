nomes = ['yasmin', 'rafael', 'jessica']

# SEM List Comprehensions
# with open('nomes.txt', 'a') as arquivo:
#     for nome in nomes:
#         arquivo.write(nome +'\n')

# COM List Comprehensions
with open('nomes.txt', 'a') as arquivo:
    arquivo.writelines([x+'\n' for x in nomes])


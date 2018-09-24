# read() ler arquivo inteiro
# readline ler linha do arquivo
# readlines ler arquivo inteiro como lista

# Append
# with open("nomes.txt", "a") as arquivo:
#     arquivo.write("Joao\n")
#     arquivo.write("Kassilas\n")

# Read
# with open("nomes.txt", "r") as arq:
#     conteudo = arq.read()
# print(conteudo)

# ReadLines
# with open("nomes.txt", "r") as arq:
#     conteudo = arq.readlines()
# for x in conteudo:
#     print(x, end="")

# Write Lines
nomes = ["pedro\n", "joao\n", "maria\n"]

with open("nomes.txt","w") as arq:
    arq.writelines(nomes)
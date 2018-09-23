novo_conteudo = []
cont = 0

#pegar conteudo
with open("nomes.txt", "r") as arq:
    conteudo = arq.readlines()

#alterar conteudo
for linha in conteudo:
    novo_conteudo.append(str(cont)+"-"+linha)
    cont += 1

#sobreescrever com novo conteudo
with open("nomes.txt", "w") as arq:
    arq.writelines(novo_conteudo)


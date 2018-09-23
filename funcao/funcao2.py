def ler_arquivo(*arquivo:str)-> int:
    '''função para ler arquivo'''
    conteudo = []
    for x in arquivo:
        with open(x, 'r')as arq:
            conteudo += arq.readlines()
    return conteudo

def escrever_arquivo(arquivo:str, conteudo:list):
    '''função para escrever no arquivo'''
    conteudo = [x+'\n' for x in conteudo]
    try:
        with open(arquivo, 'a') as arq:
            arq.writelines(conteudo)
    except Exception as e:
        print('Erro: {}'.format(e))

def contar_linhas(arquivo):
    return len(ler_arquivo(arquivo))

# a = ler_arquivo('nomes.txt')
# ler_arquivo('xxx')
# ler_arquivo('zzz')

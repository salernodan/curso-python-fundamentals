with open('nomes.txt', 'r') as arquivo:
    print(arquivo.readline())
    print(arquivo.readline())
    arquivo.seek(0)
    print(arquivo.readline())
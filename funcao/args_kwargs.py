def pessoas(*args):
    for x in args:
        print(x)

def cadastro(**kwargs):
    
    print(kwargs)

pessoas('daniel', 'pedro', 'joao')

cadastro(nome='daniel', sobrenome='prata', idade=24)
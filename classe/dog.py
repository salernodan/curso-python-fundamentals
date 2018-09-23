class Dog():
    '''Tentando abstrair um dog'''

    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.energia = 3

    #Toda vez que printar o objeto ele vai executar o __str__
    def __str__(self):
        return 'nome:{}, idade:{}, raca:{}\n'.format(self.nome,self.idade,self.raca)


    def latir(self):
        print('Au Au Au')
        self.energia -= 1
        print('energia: ',self.energia, end='\n\n')

    def comer(self):
        print('hummmm')
        self.energia += 3
        print('energia: ',self.energia, end='\n\n')

    def dormir(self):
        self.energia = 3
        print('Zzzzzzz...')

    def andar(self):
        self.energia -= 1
        print('andando...')    
    
    def renomear(self, novo_nome):
        self.nome = novo_nome
        print('Cachorro adotado')
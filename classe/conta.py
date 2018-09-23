
class Conta():

    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self._saldo = saldo

    #Deixando o saldo privado

    #Como definir propriedade
    @property
    def saldo(self):
        return self._saldo

    #Decorator
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo


    def __str__(self):
        return 'titular:{}, numero:{}, saldo:{}, tipo: Conta Corrente \n'.format(self.titular,self.numero,self.saldo)        


    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo


    def depositar(self, valor):
        self.saldo += valor
        return self.saldo


    def transferir(self, conta, valor):
        self.sacar(valor)
        conta.depositar(valor)
        

#Classe Poupanca herdando da Conta
class Poupanca(Conta):


    #Reescrevendo o metodo init
    def __init__(self, titular, numero, saldo):
        #Herda os atributos da conta
        super().__init__(titular, numero, saldo)
        #Adiciona o atribu
        self.juros = 0.005

    def __str__(self):
        return 'titular:{}, numero:{}, saldo:{}, tipo: Poupanca \n'.format(self.titular,self.numero,self.saldo)


    def render(self):
        self.saldo += self.saldo * self.juros




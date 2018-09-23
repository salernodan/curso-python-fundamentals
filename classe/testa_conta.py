from conta import Conta, Poupanca
# import conta

conta1 = Conta('daniel', 123456, 1500)
conta2 = Poupanca('maria', 654321, 1500)

conta1 = Conta('Daniel', '123-4', 10000)
conta1_poupanca = Poupanca('Daniel', '123-4/500', 0)
conta2 = Conta('Pedro', '135-5', 10000)

conta1.transferir(conta2, 500)

conta1.transferir(conta1_poupanca, 1000)
conta1_poupanca.render()

print(conta1.saldo, conta1_poupanca.saldo, conta2.saldo, sep='\n')

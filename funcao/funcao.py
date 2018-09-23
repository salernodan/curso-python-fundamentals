# def soma(x, y):
#     print(x + y)

# def soma(x:int, y:int) -> int:
#     '''Funcao que soma dois numeros'''
#     print(x + y)

# soma(2, 4)
# soma('a', 'b')

def soma(x, y):
    return x + y

a = soma(2,5)
print(a)

print(soma(soma(4, 8), soma(2, 4)))
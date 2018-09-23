def soma(x, y):
    return x + y


a = lambda x: x ** 2
a(6)

nomes = ['daniel', 'prata']
print(list(map(lambda x: x.title(), nomes)))
print(list(map(lambda y: y ** 2, range(1,11))))
# map(lambda x: x if condicao else lambda y: y, sequencia)

# verdade if condicao else falso

[x for x in range(10) if x % 2 == 0]

# quadrados = []
# for x in range(1, 11):
#     quadrados.append((lambda y: y ** 2)(x))

# print(quadrados)

# quadrados = [(lambda y: y ** 2)(x)for x in range(1, 11)]

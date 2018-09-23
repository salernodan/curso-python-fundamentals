from dog import Dog

dog1 = Dog('bilu', 2, 'SRD')
dog2 = Dog('rex', 4, 'pintcher')

print(dog1)

dog1.latir()
dog1.latir()
dog1.comer()
dog1.renomear('python')

print(dog1)

# print(dog1, dog2, sep='\n')
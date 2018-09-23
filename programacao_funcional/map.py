#!/usr/bin/python3

# map(lambda x: x**2, range(1,11))

nomes = ['daniel', 'pedro', 'maria']

print(list(map(lambda x: x.title(), nomes)))

print(list(map(lambda x: x**2, range(1,101))))
#!/usr/bin/python3
media = 8

if media >= 2:
    print('Media: {0} \nAprovado'.format(media))
elif media > 3 and media < 7:
    print('Media: {0} \nRecuperacao'.format(media))
else:
    print('Media: {0} \nReprovado'.format(media))
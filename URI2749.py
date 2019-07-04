#Linha tracejada:

for i in range(39):
    print('-', end='')
print()

# Linha de texto 1

print('|', end='')
print('x = 35', end='')
for i in range(31):
    print(' ', end='')
print('|')

#Linha em branco:

print('|', end='')
for i in range(37):
    print(' ', end='')
print('|')

# Linha "texto2"

print('|', end='')
for i in range(31):
    print(' ', end='')
    if i==14:
        print('x = 35', end='')
print('|')

#Linha em branco:

print('|', end='')
for i in range(37):
    print(' ', end='')
print('|')

# Linha "texto3"

print('|', end='')
for i in range(31):
    print(' ', end='')
    if i==30:
        print('x = 35', end='')
print('|')

#Linha tracejada:

for i in range(39):
    print('-', end='')
print()
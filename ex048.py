soma = 0
cont = 0
quebra = 0
for c in range(1,501,2):
    if c % 3 == 0:
        print('[{:3}'.format(c), end=']')
        print(',' if c < 495 else '', end='')
        soma += c
        cont += 1
        quebra += 1
        if quebra == 12:
            print()
            quebra = 0

print()
print()
print('A soma de todos os {} números acima é {}.'.format(cont, soma))

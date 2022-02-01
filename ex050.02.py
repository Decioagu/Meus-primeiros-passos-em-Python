soma = 0
for c in range(0,6):
    num = int(input('Digite o {}º número: '.format(c+1)))
    teste = num % 2
    if teste == 0:
        soma += num
print()
if soma == 0:
    print('A soma dos números pares é \033[32m{}\033[m.'.format(soma))
else:
    print('A soma dos números pares são \033[32m{}\033[m.'.format(soma))

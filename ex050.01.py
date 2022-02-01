num1 = int(input('Digite um número: '))
teste = num1 % 2
if teste != 0:
    num1 = 0
soma = 0
for c in range(0,5):
    num = int(input('Digite outro número: '))
    teste = num % 2
    if teste == 0:
        soma += num
print()
if soma + num1 == 0:
    print('A soma dos números pares é \033[32m{}\033[m.'.format(soma + num1))
else:
    print('A soma dos números pares são \033[32m{}\033[m.'.format(soma + num1))

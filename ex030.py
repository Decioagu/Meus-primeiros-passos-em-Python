n = int(input('Digite um número inteiro: '))
valor = n % 2
if valor == 0:
    print('O número {} é par!'.format(n))
else:
    print('O número {} é impar!'.format(n))
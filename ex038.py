print('\033[34m=\033[m'*43)
print('\033[35mCompare dois números e veja qual é o maior!\033[m')
print('\033[34m=\033[m'*43)
print()
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print()
menor = n1
maior = n2
if n1 > n2:
    maior = n1
    menor = n2
if maior == menor:
    print('Os valores são iguais a {}{}{}.'.format('\033[32m', maior, '\033[m'))
else:
    print('O maior número é {}{}{}.'.format('\033[32m', maior, '\033[m'))
    print('O menor número é {}{}{}.'.format('\033[32m', menor, '\033[m'))

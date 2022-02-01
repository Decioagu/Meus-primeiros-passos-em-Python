print('Digite 3 números inteiros e veja qual é o maior e o menor.')
print()
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print()
maior = menor = n1
if n2 <= n1 and n2 <= n3:
    menor = n2
if n3 <= n1 and n3 <= n2:
    menor = n3
if n2 >= n1 and n2 >= n3:
    maior = n2
if n3 >= n1 and n3 >= n2:
    maior = n3
if maior == menor:
    print('Todos os valores são iguias a {}'.format(maior))
else:
    print('O maior número é ', maior)
    print('O menor número é ', menor)

print('Digite 3 números inteiros e veja qual é o maior e o menor.')
print()
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print()
if n1 <= n2 < n3:
    print('O maior número é ', n3)
    print('O menor número é ', n1)
elif n1 >= n2 > n3:
    print('O maior número é ', n1)
    print('O menor número é ', n3)
elif n2 > n1 and n3 >= n1:
    print('O maior número é ', n2)
    print('O menor número é ', n1)
elif n2 > n3 and n1 >= n3:
    print('O maior número é ', n2)
    print('O menor número é ', n3)
elif n2 < n1 and n3 <= n1:
    print('O maior número é ', n1)
    print('O menor número é ', n2)
elif n2 < n3 and n1 <= n3:
    print('O maior número é ', n3)
    print('O menor número é ', n2)
else:
    print('Todos os valores são iguais!!!')

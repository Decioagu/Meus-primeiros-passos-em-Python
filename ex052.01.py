print('NÚMERO PRIMO')
print()
n = int(input('Digite um número inteiro: '))
print()
primo = 0
if n >=2:
    if n == 2:
        print(f'Número {n}, é PRIMO!!!')
    else:
        for c in range(2,n):
            teste = n % c
            if teste == 0:
                primo += 1
        if primo == 0:
            print(f'Número {n}, é PRIMO!!!')
        else:
            print('Número {n}, NÃO é PRIMO!!!')
else:
    print(f'Número {n} inválido, digite um número maior ou igual a "2".')

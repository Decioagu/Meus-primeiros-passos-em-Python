print('NÚMERO PRIMO')
print()
n = int(input('Digite um número inteiro: '))
print()
if n >= 2:
    cont = 0
    for c in range(1, n+1):
        if n % c == 0:
            cont+=1
    if cont == 2:
        print(f"{n} é primo")
    else:
        print(f"{n} NÃO é primo")
else:
    print(f'Número {n} inválido, digite um número maior ou igual a "2".')


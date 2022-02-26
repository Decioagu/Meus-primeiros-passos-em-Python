print('NÚMERO PRIMO')
print()
n = int(input('Digite um número inteiro: '))
print()
primo = []
if n >=2:
    for t in range(1, n+1):
        cont = 0
        for c in range(1,n+1):
            if t % c == 0:
                cont+=1
        if cont == 2:
            primo.append(t)
    print(primo)
else:
    print(f'Número {n} inválido, digite um número maior ou igual a "2".')


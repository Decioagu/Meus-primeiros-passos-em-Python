from time import sleep
from random import randint
numeros = []


def titulo(txt):
    print(f'=' * (len(txt) + 4))
    print(f'= {txt} =')
    print(f'=' * (len(txt) + 4))


def sorteia():
    cont = 0
    for quant in range(0, 5):
        num = randint(0, 9)
        numeros.append(num)

    print(f'Sorteados {len(numeros)} valores na lista: ', end='')
    for n in numeros:
        cont += 1
        if cont == len(numeros):
            print(n, end='.\n')
        elif cont == (len(numeros) - 1):
            print(n, end=' e ')
        else:
            print(n, end=', ')
        sleep(0.5)


def somaPar():
    soma = cont = contPar = 0
    for n in numeros:
        if n % 2 == 0:
            contPar += 1
    if contPar == 0:
        print(f'Não há valores PARES na lista.')
    elif contPar == 1:
        print(f'O único valor PAR é ', end='')
        for n in numeros:
            if n % 2 == 0:
                print(f'{n}.')
    else:
        print(f'Somando os valores PARES: ', end='')
        for n in numeros:
            if n % 2 == 0:
                soma += n
                cont += 1
                if cont == contPar:
                    print(n, end=' = ')
                else:
                    print(n, end=' + ')
        print(f'{soma}.')

titulo('Funções para sortear e somar'.upper())
print()
sorteia()
somaPar()

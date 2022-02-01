from time import sleep
from random import randint


def titulo(txt):
    print(f'=' * (len(txt)))
    print(f'{txt}')



titulo(' Função que descobre o maior '.center(63, '=').upper())

# def sorteio(x):


lista = []
cont = 0


for repet in range(0, randint(1, 9)):
    print('=' * 63)
    print('Analisando os valores...')
    for quant in range(0, randint(1, 9)):
        num = randint(0, 9)
        lista.append(num)
    for l in lista:
        cont += 1
        if cont == len(lista):
            print(l, end='. ')
        elif cont == (len(lista) - 1):
            print(l, end=' e ')
        else:
            print(l, end=', ')
        sleep(0.5)

    if len(lista) <=1:
        print(f'Foi informado {len(lista)} valor ao todo.')
    else:
        print(f'Foram informados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi {max(lista)}.')
    cont = 0
    lista.clear()
print('=' * 63)



from time import sleep


def titulo(txt):
    print(f'=' * (len(txt)))
    print(f'{txt}')



titulo(' Função que descobre o maior '.center(63, '=').upper())


def maior(* num):
    cont = maior = 0
    print('=' * 63)
    print('Analisando os valores...')
    for c in num:
        cont += 1
        print(c, end='')
        sleep(0.5)
        if cont == len(num):
            print(end='. ')
        elif cont == (len(num) - 1):
            print(end=' e ')
        else:
            print(end=', ')
        if cont == 1:
            maior = c
        if maior < c:
            maior = c

    if len(num) <= 1:
        print(f'Foi informado {len(num)} valor ao todo.')
    else:
        print(f'Foram informados {len(num)} valores ao todo.')

    print(f'O maior valor informado foi {maior}.')


maior(3, 6, 9, 8, 4, 2)
maior(7, 5, 1, 6)
maior(5, 7)
maior(2)
maior()
print('=' * 63)
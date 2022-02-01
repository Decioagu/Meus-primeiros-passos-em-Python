from time import sleep


def teste_int(num):
    teste = num
    while True:
        if teste.count('-') == 1:
            teste = teste.replace('-', '')
            if teste.isnumeric():
                teste = '-' + teste
                num = int(teste)
                break
        else:
            if teste.isnumeric():
                num = int(teste)
                break
            else:
                print(f'Erro...')
                print(f'Favor digitar apenas valores numéricos inteiros.')
                print()
            teste = input(f'Digite um valor NUMÉRICO INTEIRO: ').strip()
    return num


def titulo(txt):
    print(f'=' * (len(txt) + 27))
    print(f' {txt} '.center(45, '='))


titulo('Função de Contador'.upper())
cont = 0


def contador(i, f, p):
    print(f'Contagem de {i} até {f} passo de {p} em {p}')
    if p == 0:
        print('Erro...')
        print('O passo tem de ser ≠ de zero!')

    elif i == f:
        print(i, end=' ')
        sleep(0.5)
        print('Fim!')

    else:
        cont = i
        if p < 0:
            p *= -1
        if i < f:
            while cont <= f:
                print(cont, end=' ', flush=True) # Uso de "flush" caso "sleep" não funcione
                sleep(0.5)
                cont += p
            print('Fim!')
        if i > f:
            while cont >= f:
                print(cont, end=' ', flush=True) # Uso de "flush" caso "sleep" não funcione
                cont -= p
                sleep(0.5)
            print('Fim!')
    print('=' * 45)


print('='*45)
contador(1, 10, 1)
contador(10, 0, 2)

while True:
    print('Agora é sua vez de personalizar a contagem!')
    inicio = input('Inicio = ')
    inicio = teste_int(inicio)
    fim = input('Fim = ')
    fim = teste_int(fim)
    passe = input('Passe = ')
    passe = teste_int(passe)
    contador(inicio, fim, passe)



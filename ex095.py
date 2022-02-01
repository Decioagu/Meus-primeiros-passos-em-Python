print('='*40)
print(' IMPRESSÃO DE DADOS DE UM DIOCIONÁRIO '.center(40, '='))
print('='*40)

lista = []
gols = []
dicionario = {}

print()
while True:
    dicionario['nome'] = input('Nome do jogador: ').strip().upper()

    while True:
        partidas = (input(f'Quantas partidas {dicionario["nome"]} jogou? '))
        if partidas.isnumeric() == True:
            partidas = int(partidas)
            break
        else:
            print('Erro! Digite apenas valores númericos.')

    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na {c + 1}ª partida? ')))
    dicionario['gols'] = gols.copy()

    total = sum(gols)
    dicionario['total'] = total

    lista.append(dicionario.copy())
    dicionario.clear()
    gols.clear()

    while True:
        opcao = input('Você quer contunuar? [S/N] ').strip().upper()
        if opcao in 'NS':
            print()
            break
        else:
            print('Informação invalida!')
            print('Digite "S" para CONTINUAR ou "N" para FINALIZAR.')

    if opcao == 'N':
        break


print(' LISTA DE JOGADORES '.center(60, '='))
print('Cód:  Nome:               Gols:               Total de gols:')

for p, l in enumerate(lista):
    print(f'{p + 1}     ', end='')
    for v in l.values():
        print(f'{str(v):<20}', end='')
    print()
print('=' * 60)
print()

while True:
    while True:
        cod = input('Gostaria de ver os dados de qual jogador, digite o "Cód":')
        if cod.isnumeric() == True:
            cod = int(cod)
            break
        else:
            print('Erro! Digite apenas valores númericos conforme "Cód" apresentado.')
            print()

    if 0 < cod <= len(lista):
        print('=' * 40)
        print(f'Dados do jogador:  {lista[cod-1]["nome"]} ')
        for p, g in enumerate(lista[cod-1]['gols']):
            if g == 0:
                print(f'No {p + 1}º jogo não fez gol')
            elif g == 1:
                print(f'No {p + 1}º jogo fez {g} gol')
            else:
                print(f'No {p + 1}º jogo foram {g} gols')
        if lista[cod-1]["total"] == 0:
            print('Não marcou nenhum gol...')
        else:
            print(f'Total de {lista[cod - 1]["total"]} gols: {"⚽" * lista[cod - 1]["total"]} ')

        print('=' * 40)
    else:
        print()
        print(f'Não exite jogador "Cód" = {cod}.')
        print(f'Consulte a LISTA DE JOGADORES acima e escolha um novo "Cód".')

    while True:
        opcao = input('Você quer contunuar? [S/N] ').strip().upper()
        if opcao in 'NS':
            print()
            break
        else:
            print()
            print('Informação invalida!')
            print('Digite "S" para CONTINUAR ou "N" para FINALIZAR.')

    if opcao == 'N':
        break
print()
print(lista)

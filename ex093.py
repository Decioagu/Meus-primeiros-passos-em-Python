print('='*40)
print(' IMPRESSÃO DE DADOS DE UM DIOCIONÁRIO '.center(40, '='))
print('='*40)

lista = []
gols = []
dicionario = {}

dicionario['nome'] = input('Nome do jogador: ')

partidas = int(input(f'Quantas partidas {dicionario["nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na {c + 1}ª partida? ')))
dicionario['gols'] = gols.copy()

total = sum(gols)
dicionario['total'] = total

lista.append(dicionario.copy())
print('=' * 60)
print(lista)
print('=' * 60)
print(f'O campo nome tem o valor {dicionario["nome"]}.')
print(f'O campo gols tem o valor {dicionario["gols"]}.')
print(f'O campo total tem o valor {dicionario["total"]}.')
print('=' * 60)
print(f'O jogador {dicionario["nome"]} jogou {partidas} partidas.')
for k, c in enumerate(dicionario['gols']):
    if c <= 1:
        print(f'Na {k + 1}ª partida, foi {c} gol')
    else:
        print(f'Na {k + 1}ª partida, foram {c} gols')

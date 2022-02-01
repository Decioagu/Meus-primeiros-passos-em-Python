limpa = '\033[m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
cinza = '\033[37m'
neg = '\033[1m'
sub = '\033[4m'
inv = '\033[7m'
print()
print('COMPARAÇÃO DE PESO')
print()
print('Digite o peso de  5 pessoa e veja quem é o mais pesado e o mais magro.')
print()
lista = []
for c in range(0, 5):
    peso = float(input('Digite o peso da {}ª pessoa em Kg: '.format(c+1)))
    lista.append(peso)
    lista.sort()
print()
print('O {0}maior{1} peso é {0}{2:.2f}Kg{1}.'.format(vermelho, limpa, lista[-1]))
print('O {0}menor{1} peso é {0}{2:.2f}Kg{1}.'.format(verde, limpa, lista[0]))

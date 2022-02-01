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
print('MAIOR IDADE')
print()
print('Digite a data de aniversario de 7 pessoa e veja quem é maior de idade...')
print()
from datetime import date
ano = date.today().year
maioridade = 0
menoridade = 0
for c in range(0, 7):
    aniversario = int(input('Digite o ano de aniversario da {}ª pessoa: '.format(c+1)))
    idade = ano - aniversario
    if idade >= 21:
        maioridade += 1
    elif 0 <= idade < 21:
        menoridade += 1
    else:
        print('Esta idade NÃO é valida...')
print()
print('Maior de idade = {}'.format(maioridade))
print('Menor de idade = {}'.format(menoridade))


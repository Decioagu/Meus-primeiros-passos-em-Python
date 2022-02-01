limpa = '\033[m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
print('\033[36m=\033[m'*7)
print('{}Boletim{}'.format(roxo, limpa))
print('\033[36m=\033[m'*7)
print()
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print()
media = (n1 + n2) / 2
if media < 5:
    print('Sua média foi {0}{2:.2f}{1}, você foi '
          '{0}REPROVADO{1}!!!'.format(vermelho, limpa, media))
elif 7 > media >= 5:
    print('Sua média foi {0}{2:.2f}{1}, você esta em '
          '{0}RECUPERAÇÃO{1}!!!'.format(amarelo, limpa, media))
else:
    print('Sua média foi {0}{2:.2f}{1}, você esta '
          '{0}APROVADO{1}!!!'.format(verde, limpa, media))
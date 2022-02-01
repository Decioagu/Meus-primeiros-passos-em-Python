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
print('INFORMAÇÕES')
print()
somaidade = 0
homenvelhoidade = 0
homenvelhonome = ''
mulhernovaidade = 0
mulhernovanome = []
contadorhomem = 0
contadormulher = 0

for c in range(0, 4):
    print('{:^40}'.format('{1}{2}ª PESSOA{0}').format(limpa, ciano, c + 1))
    nome = input('NOME: ').strip().upper()
    idade = input('{}IDADE{}: '.format(amarelo, limpa))
    if idade.isnumeric() == True:
        idade = int(idade)
    else:
        while idade.isnumeric() == False:
            print('Preencha apenas com dados numéricos.')
            idade = input('{}IDADE{}: '.format(amarelo, limpa))
        idade = int(idade)
    sexo = input('SEXO [{1}H{0}/{2}M{0}]: '.format(limpa, azul, roxo)).strip().upper()
    somaidade += idade

    while sexo != 'H' and sexo != 'M':
        print('Opção invalida, digite {1}"{4}H{0}{1}"{0} para {1}{3}homem{0} e '
              '{2}"{4}M{0}{2}"{0} para {2}{3}mulher{0}.'.format(limpa, azul, roxo, sub, neg))
        sexo = input('SEXO [{1}H{0}/{2}M{0}]: '.format(limpa, azul, roxo)).strip().upper()

    if homenvelhoidade < idade and sexo == 'H':
        contadorhomem += 1
        homenvelhoidade = idade
        homenvelhonome = nome

    if idade < 20 and sexo == 'M':
        contadormulher += 1
        mulhernovanome.append(nome)

mediaidade = somaidade/4

print('A média da idade do grupo é {1}{2} '
      'anos{0}.'.format(limpa, amarelo, mediaidade))

if contadorhomem != 0:
    print('O homem mais velho tem {1}{2}{0} e se chama '
          '{1}{3}{0}.'.format(limpa, azul, homenvelhoidade, homenvelhonome))

if contadormulher == 1:
    print('Neste grupo só há {0}uma mulher menor de 20 anos{1} '
          'e seu nome é {0}{2}{1}.'.format(roxo, limpa, mulhernovanome[0]))

elif contadormulher > 1:
    print('Neste grupo temos {1}{2} mulheres menores de 20 anos{0}.'.format(limpa, roxo, contadormulher))
    print('{}Elas são:{}'.format(roxo, limpa))
    for x in range(0, contadormulher):
        print('{1}Nome: {2}{0}'.format(limpa, roxo, mulhernovanome[x]))
else:
    print('Neste grupo {1}NÃO{0} tem {2}{1}nenhuma MULHER{0} com menos de {1}20 anos{0}.'.format(limpa, vermelho, sub))

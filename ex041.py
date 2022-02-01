from datetime import date
limpa = '\033[m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[4;34m'
roxo = '\033[35m'
ciano = '\033[36m'
print('\033[35m=\033[m'*32)
print('{}CONFEDERAÇÃO NACIONAL DE NATAÇÃO{}'.format(ciano, limpa))
print('\033[35m=\033[m'*32)
print()
nome = input('Informe o nome do participante: ')
nome = nome.upper().strip()
idade = int(input('Informe o ano de nascimento do participante: '))
ano = date.today().year
classe = ano - idade
categ = 'MASTER'
if classe <= 9:
    categ = 'MIRIM'
if 9 < classe <= 14:
    categ = 'INFANTIL'
if 14 < classe <= 19:
    categ = 'JUNIOR'
if classe == 20:
    categ = 'SÊNIOR'
print('{0}{2}{1} esta classificado(a) na categoria '
      '{0}{3}{1}.'.format(azul, limpa, nome, categ))

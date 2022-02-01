limpa = '\033[m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
cinza = '\033[37m'
sub = '\033[4m'
neg = '\033[1m'
inv = '\033[7m'


print()
print('{0}P{1}rogressão {0}A{1}ritmética ({0}P.A.{1})'.format(azul,limpa,inv))
print()
print('''Fórmula do termo geral:

{4}1º formula{0}:
{1}an{0} = {2}a1{0} + ({3}n{0}-{2}1{0}){4}r{0}

{1}an{0}: termo que queremos calcular
{2}a1{0}: primeiro termo da {2}P.A.{0}
{3}n{0}: posição do termo que queremos descobrir
{4}r{0}: razão

"OU"

{4}2º formula{0}:
{1}an{0} = {2}ak{0} + ({3}n{0}-{2}k{0}){4}r{0}

{1}an{0}: o {2}n{0}-ésimo termo da {2}P.A.{0} (um termo numa posição {2}n{0} qualquer)
{2}ak{0}: o {2}k{0}-ésimo termo de uma {2}P.A.{0} (um termo numa posição {2}k{0} qualquer)
{4}r{0}: a razão

Repare que a única diferença, foi a mudança do índice {2}{6}1{0} na {5}{4}1º fórmula{0}, pelo {2}{6}k{0}, na {5}{4}2º fórmula{0}.'''.format(limpa, vermelho, azul, verde, roxo, sub, neg))
print()
a1 = int(input('Digite o Primeiro Temo: '))
r = int(input('Digite a Razão: '))
lista = []
an = a1 + (10-1)*r
c = a1
print()
while c != an:
    lista.append(c)
    c = c + r
print('{1}PA{0} = {2}{0}'.format(limpa, azul, lista))

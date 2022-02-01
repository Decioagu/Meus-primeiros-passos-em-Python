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

from time import sleep

print()
print('{}PALINDROMO{}'.format(roxo, limpa))
print()
print('''Um {2}palíndromo{0} é uma palavra, frase ou qualquer outra
sequência de caractere que tenha a propriedade de poder ser lida 
tanto da direita para a esquerda como da esquerda para a direita.
{3}EXEMPLOS{0}:
"{1}ANA{0}"
"{1}A SACADA DA CASA{0}"
"{1}A TORRE DA DERROTA{0}"
"{1}O LOBO AMA O BOLO{0}"
"{1}ANOTARAM A DATA DA MARATONA{0}"'''.format(limpa, verde, roxo, amarelo))
print()
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
invesor = ''
for letra in range(len(junto) - 1, -1, -1):
    invesor += junto[letra]
print()
print('{}PROCESSANDO...{}'.format(amarelo, limpa))
sleep(1)
print()
if junto == invesor:
    print('Seu texto é um {1}PALINDROMO{0}!!!'.format(limpa, verde))
    print('{2}{0} = {1}{3}'.format(junto, invesor, verde, limpa))
else:
    print('Seu texto é {1}NÃO{0} é um {1}PALINDROMO{0}!'.format(limpa, vermelho))
    print('{2}{0} ≠ {1}{3}'.format(junto, invesor, vermelho, limpa))

limpa = '\033[m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
sub = '\033[4m'
negrito = '\033[1m'
from time import sleep
print('\033[36m-=-\033[m'*10)
print('{:^33}'.format('{}SMART TV{}').format(roxo, limpa))
print('\033[36m-=-\033[m'*10)
preço = float(input('Informe o preço do produto R$'))
print()
print('{}Segue abaixo as condições de pagamento:{}'.upper().format(roxo, limpa))
print('[1] = {3}{1}À VISTA{0} EM {1}DINHEIRO{0} OU {1}DEBITO{0}: {1}desconto '
      'de 10%{0}, preço {1}R${2:.2f}{0}'.format(limpa, verde,
                                                preço - (preço*10/100), sub))
print('[2] = {1}1x NO CREDITO{0}: {2}desconto de 5%{0}, '
      'preço {2}R${3:.2f}{0}'.format(limpa, amarelo, verde,
                                     preço - (preço*5/100)))
print('[3] = {1}2x NO CREDITO{0}: {2}{4}{5}sem desconto{0}, preço '
      '{2}R${3:.2f}{0}'.format(limpa, amarelo, azul, preço, negrito, sub))
print('[4] = {1}3x NO CREDITO{0}: {2}juros de 20%{0}, preço '
      '{2}R${3:.2f}{0}'.format(limpa, amarelo, vermelho, preço + (preço*20/100)))
pagamento = int(input('Qual a opção de pagamento?'))
print('PROCESSANDO...')
sleep(2)
if pagamento == 1:
    print('Pagamento {1}{3}À VISTA{0}, {1}desconto de 10%{0}, valor da compra '
          '{1}R${2:.2f}{0}'.format(limpa, verde, preço - (preço*10/100), sub))
elif pagamento == 2:
    print('Pagamento {1}1x NO CREDITO{0}, {2}desconto de 5%{0}, valor da compra '
          '{2}R${3:.2f}{0}'.format(limpa, amarelo, verde, preço - (preço*5/100)))
elif pagamento == 3:
    print('Pagamento {1}2x NO CREDITO{0}, valor {4}{5}{6}TOTAL{0} da compra '
          '{6}R${3:.2f}{0} em {6}{5}2x de R${2:.2f}{0}'.format(limpa, amarelo, preço/2,
                                                               preço, negrito, sub, azul))
elif pagamento == 4:
    print('Pagamento {1}3x NO CATÃO{0}, valor {5}{6}{2}TOTAL{0} da compra '
          '{2}R${3:.2f}{0} em {5}{6}{2}3x de R${4:.2f}{0}'.format(limpa, amarelo, vermelho,
                                                                  preço + (preço*20/100),
                                                                  (preço + (preço*20/100))/3,
                                                                  negrito, sub))
else:
    print('{}{}Opção invalida!!!'.format(negrito, vermelho))
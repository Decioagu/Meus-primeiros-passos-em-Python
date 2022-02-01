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
print('CRECK!!!')
sleep(1)
print(' Xiiiiiii..')
sleep(1)
print('   Chuuuuuu...')
print()
for c in  range(3, 0, -1):
    print(c)
    sleep(1)
print('Pa.')
print(' {}Papa..{}'.format(amarelo, limpa))
print('  {}Papa..{}'.format(verde, limpa))
print('   {}Papapa...{}'.format(azul, limpa))
print('    {}Papapapa....{}'.format(roxo, limpa))
sleep(2)
print('     {}Boooooooom....{}'.format(vermelho, limpa))
sleep(1)
print('      {}Rojão 13 tiros...'.upper().format(ciano))


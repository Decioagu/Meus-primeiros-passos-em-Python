print('='*26)
print('CONVERSOR DE BASE NUMÉRICA')
print('='*26)
print()
num = int(input('Digite um número inteiro: '))
print()
print('''Escolha as opções abaixo para conversão: 
\033[36m[1]\033[m = para base \033[36mBINÁRIO\033[m
\033[34m[2]\033[m = para base \033[34mOCTAL\033[m
\033[35m[3]\033[m = para base \033[35mHEXADECIMAL\033[m''')
op = int(input('Digite sua opção:'))
print()
if op == 1:
    print('Número \033[32m{}\033[m convertido para \033[36mBINÁRIO'
          '\033[m = \033[36m{}\033[m'.format(num, bin(num)[2:]))
elif op == 2:
    print('Número \033[32m{}\033[m convertido para \033[34mOCTAL'
          '\033[m = \033[34m{}\033[m'.format(num, oct(num)[2:]))
elif op == 3:
    print('Número \033[32m{}\033[m convertido para \033[35mHEXADECIMAL'
          '\033[m = \033[35m{}\033[m'.format(num, str(hex(num)).upper()[2:]))
else:
    print('\033[31mFoi digitada uma opção invalida!\033[m')

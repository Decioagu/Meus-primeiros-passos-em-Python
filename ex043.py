print('\033[36m-=-\033[m'*8)
print('\033[35m     CALCULO DE IMC\033[m')
print('\033[36m-=-\033[m'*8)
kg = float(input('Digite o seu peso em Kg: '))
m = float(input('Digite a sua altura em metro: '))
print()
imc = kg / (m**2)
peso = '\033[1;4;31mobesidade mórbida\033[m'
print('{:=^14}'.format('Tabela IMC'))
print('''\033[36mMagro\033[m: \033[4;36mabaixo de\033[m \033[32m18.5Kg/m²\033[m
\033[32mNormal\033[m: \033[32m18.5 até 25Kg/m²\033[m
\033[33mSobrepeso\033[m: \033[4;33macima de 25\033[m \033[33maté 30Kg/m²\033[m
\033[31mObesidade\033[m: \033[4;31macima de 30\033[m \033[31maté 40Kg/m²\033[m
\033[1;4;31mObesidade mórbida\033[m: \033[1;4;31macima de 40\033[m\033[31mKg/m²\033[m''')
print()
if imc < 18.5:
    cor = '\033[36m{:.2f}Kg/m²\033[m'.format(imc)
    peso = '\033[36mmagra\033[m'
elif imc <= 25:
    cor = '\033[32m{:.2f}Kg/m²\033[m'.format(imc)
    peso = '\033[32mnormal\033[m'
elif imc <= 30:
    cor = '\033[33m{:.2f}Kg/m²\033[m'.format(imc)
    peso = 'com \033[33msobrepeso\033[m'
elif imc <= 40:
    cor = '\033[31m{:.2f}Kg/m²\033[m'.format(imc)
    peso = '\033[31mobesa\033[m'
else:
    cor = '\033[31m{:.2f}Kg/m²\033[m'.format(imc)
    peso = 'com \033[1;4;31mobesidade mórbida\033[m'

print('Seu \033[35mIMC\033[m é {}, conforme a tabela acima você '
      'é uma pessoa {}!'.format(cor, peso))

from datetime import date
vermelho = '\033[31m'
limpa = '\033[m'
print('\033[34m=\033[m'*27)
print('\033[1;36mSERVIÇO MILITAR OBRIGATÓRIO\033[m')
print('\033[34m=\033[m'*27)
print()
aniver = int(input('Informe a data de seu nascimento: '))
print()
ano = date.today().year # informa data do ano atual
n = ano - aniver
if n == 17:
    print('Falta \033[33mUM ANO\033[m para \033[31mVOCÊ\033[m se '
          'apresentar ao serviço militar.')
elif n == 18:
    print('\033[31mVOCÊ\033[m deve se apresentar ao serviço militar.')
elif n < 0:
    print('Esta data \033[31mNÃO\033[m é valida!')
elif n > 18:
    print('Já passou {0}{2}{1} anos da data para se apresentar ao serviço '
          'militar.'.format(vermelho, limpa, ano - (18 + aniver)))
    print('Você deveria ter se apresentado no ano de '
          '{}{}{}.'.format(vermelho, aniver + 18, limpa))
else:
    print('Faltam \033[33m{} anos\033[m para você se apresentar ao '
          'serviço militar.'.format(18 - n))

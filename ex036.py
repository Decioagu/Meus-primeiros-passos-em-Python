cores = {'limpa': '\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m',
         'amarelo': '\033[33m', 'azul': '\033[34m', 'roxo': '\033[35m',
         'ciano': '\033[36m'}
print('\033[34m=\033[m'*29)
print('{}FINANCIAMENTO DA CASA PRÓPRIA{}'.format(cores['ciano'],
                                                 cores['limpa']))
print('\033[34m=\033[m'*29)
print()
casa = float(input('Informe o valor do imóvel , R$'))
salario = float(input('Informe o valor da renda R$'))
meses = int(input('Informe o tempo "meses" de financiamento:'))
#juros = ???
prestação = casa / meses
print()
if prestação > salario*30/100:
    print('Seu financiamento não foi aprovado.')
    print('Valor da prestação exede 30% do salorio de '
          'R${}{:.2f}{}, valor mínimo do salario '
          'R${}{:.2f}{}'.format(cores['vermelho'],
                                salario, cores['limpa'],
                                cores['amarelo'],
                                prestação*100/30,
                                cores['limpa']))
    print('Verifique com o seu corretor a possibilidade de '
          'aumento de tempo do financiamento para '
          '{}{}{} meses.'.format(cores['verde'],
                                 int(casa/(salario*30/100)),
                                 cores['limpa']))
else:
    print('\033[35mPARABÉNS!!!\033[m')
    print('Seu financiamento foi aprovado, valor da prestação mensal é de '
          'R${}{:.2f}{} fixar sem juros.'.format(cores['ciano'],
                                                 prestação,
                                                 cores['limpa']))
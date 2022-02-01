# TABELA DE CORES
limpar = '\033[m'
vermelho_claro = '\033[91m'
verde_claro = '\033[92m'
amarelo_claro = '\033[93m'
azul_claro = '\033[94m'
roxo = '\033[35m'
# FIM DA TABELA DE CORES

import moeda9
moeda9.titulo('Formatando Moedas em Python'.upper())
print()
valor = input(f'Digite o preço: {verde_claro}R${limpar}')
valor = moeda9.teste_float(valor)
print(f'A {roxo}metade{limpar} de {moeda9.moeda(valor)} é {moeda9.metade(valor)}')
print(f'A {roxo}dobro{limpar} de {moeda9.moeda(valor)} é {moeda9.dobro(valor)}')
print(f'{roxo}Aumento{limpar} de {amarelo_claro}10%{limpar} no valor de {moeda9.moeda(valor)} é {moeda9.aumento(valor)}')
print(f'{roxo}Redução{limpar} de {amarelo_claro}10%{limpar} no valor de {moeda9.moeda(valor)} é {moeda9.redução(valor)}')
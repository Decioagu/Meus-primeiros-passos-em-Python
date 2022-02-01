# TABELA DE CORES
limpar = '\033[m'
vermelho_claro = '\033[91m'
verde_claro = '\033[92m'
amarelo_claro = '\033[93m'
azul_claro = '\033[94m'
roxo = '\033[35m'
# FIM DA TABELA DE CORES

import moeda10
moeda10.titulo('Reduzindo ainda mais seu programa'.upper())
print()
valor = input(f'Digite o preço: {verde_claro}R${limpar}')
valor = moeda10.teste_float(valor)
print()
moeda10.resumo(valor, 15, 20)
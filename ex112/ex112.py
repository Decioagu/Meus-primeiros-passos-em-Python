# TABELA DE CORES
limpar = '\033[m'
vermelho_claro = '\033[91m'
verde_claro = '\033[92m'
amarelo_claro = '\033[93m'
azul_claro = '\033[94m'
roxo = '\033[35m'
# FIM DA TABELA DE CORES

from utilidadesCeV import cor12
from utilidadesCeV import moeda12
moeda12.titulo('Entrada de dados monetários'.upper())
print()
valor = input(f'Digite o preço: {verde_claro}R${limpar}').strip()
valor = moeda12.teste_float(valor)
print()
moeda12.resumo(valor)
print(f'{cor12.azul_claro}Décio Santana deAguiar{cor12.limpar}')

# TABELA DE CORES
limpar = '\033[m'
vermelho_claro = '\033[91m'
verde_claro = '\033[92m'
amarelo_claro = '\033[93m'
azul_claro = '\033[94m'
roxo = '\033[35m'
# FIM DA TABELA DE CORES

from utilidadesCeV import moeda11
moeda11.titulo('Transformando módulos em pacotes'.upper())
print()
valor = input(f'Digite o preço: {verde_claro}R${limpar}').strip()
valor = moeda11.teste_float(valor)
print()
moeda11.resumo(valor, 50, 10)



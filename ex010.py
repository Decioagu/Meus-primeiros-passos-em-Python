# Conversor de Moedas
nome = input('Digite seu nome: ')
n = float(input('Quanto de dinheiro você tem na carteira? R$:'))
print('{}, isso vale apenas US$:{:.2f} em dollar.'.format(nome, n/3.27))

# Calculando Descontos
v = float(input('Valor R$:'))
d = int(input('Desconto em porcentagem: '))
print('Pagamento a vista sai com {}% de desconto.'.format(d))
print('O valor total sai por R$:{:.2f}'.format(v-(v*d/100)))

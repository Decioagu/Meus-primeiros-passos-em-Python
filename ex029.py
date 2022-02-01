km = float(input('Qual a velocidade do carro que acabou de passar? '))
print('{:.0f}Km/h, porque?'.format(km))
if km > 80:
    print('Xiii... Vai levar uma multa de R${:.2f}'.format((km-80)*7))
else:
    print('Nada não...')
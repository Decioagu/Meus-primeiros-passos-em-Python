# Pintando área de uma Parede
alt = float(input('Qual a altura de sua parede (metros)? '))
larg = float(input('Qual a largura de sua parede (metros)? '))
area = alt*larg
print('Dimensão da parede é de {:.2f} x {:.2f}'.format(alt, larg))
print('A área de sua parede é de {:.2f}m², você vai precisar de {:.2f} litros de tinta.'.format(area, area/2))

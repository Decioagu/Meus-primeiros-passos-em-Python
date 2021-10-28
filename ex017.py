# Catetos e Hipotenusa

from math import sqrt
print('Vamos calcular a hipotenusa de um triangulo retângulo!')
print()

cat_opost = float(input('Digite o cateto oposto: '))
cat_adj = float(input('Digite o cateto adjacente: '))

print()
print('A formula consiste em (c²= a² + b²), onde:')
print('c = Hipotenusa')
print('a = Cateto oposto')
print('b = Cateto adjacente')

hipot = sqrt(cat_opost**2 + cat_adj**2)

print()
print('Hipotenusa = {:.2f}'.format(hipot))

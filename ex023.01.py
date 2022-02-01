n = int(input('Digite um número de 0 à 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('unidade:',u)
print('dezena:',d)
print('centena:',c)
print('milhar:',m)
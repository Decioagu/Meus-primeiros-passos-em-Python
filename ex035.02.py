print('Digite três valores para formar um triângulo.')
print()
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n1:
    print('Com os valores {}, {} e {}, é possível formar um triângulo.'.format(n1, n2, n3))
else:
    print('Com os valores {}, {} e {}, NÃO é possível formar um triângulo.'.format(n1, n2, n3))

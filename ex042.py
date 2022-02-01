limpa = '\033[m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
print('{}Digite três valores para formar um triângulo{}'.upper().format(roxo, limpa))
print()
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print()
if (-(n2 - n3)) < n1 < n2 + n3:
    print('Com os valores {0}{4}{3}, {1}{5}{3} e {2}{6}{3}, '
          'é possível formar um triângulo.'.format(azul, ciano, verde,
                                                   limpa, n1, n2, n3))
    if n1 == n2 == n3:
        print('Estes valores corresponde a um triângulo '
              '{}EQUILÁTERO{}!'.format(roxo, limpa))
    elif n1 != n2 != n3 != n1:
        print('Estes valores corresponde a um triângulo '
              '{}ESCALENO{}!'.format(roxo, limpa))
    else:
        print('Estes valores corresponde a um triângulo '
              '{}ISÓSCELES{}!'.format(roxo, limpa))
else:
    print('Com os valores {0}{5}{4}, {1}{6}{4} e {2}{7}{4}, {3}NÃO{4} '
          'é possível formar um triângulo.'.format(azul, ciano, verde,
                                                   vermelho, limpa,
                                                   n1, n2, n3))

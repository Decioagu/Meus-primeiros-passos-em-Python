# Parte inteira de um número

# Chamada biblioteca de matemática ,"math"
from math import trunc
n = float(input('Digite um número em decimal: '))
print('{} ='.format(n), type(n))

# Uso da função "trunc"
print('Inteiro truncado = {}'.format(trunc(n))) # Print valor apos ponto sem arrendondamento

# Formatação de apresentação de print em ponto flutuante
print('Inteiro formatado = {:.0f}'.format(n)) # Arredonda valores "n" para cima ou para baixo apos valor "n.5"





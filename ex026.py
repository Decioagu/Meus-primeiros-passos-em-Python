frase = input('Digite uma frase: ')
frase = frase.strip()
frase = frase.lower()
a = frase.count('a')
inicio = frase.find('a') + 1
fim = frase.rfind('a') + 1
print('A letra "a" aparece {} vezes na frase'.format(a))
print('A primeira letra "a" aparece em na posição {}'.format(inicio))
print('A ultima letra "a" aparece em na posição {}'.format(fim))

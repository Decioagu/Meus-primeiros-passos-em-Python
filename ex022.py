# Analisador de Textos
print('Bom dia!')
nome = input('Por favor digite seu nome completo: ')
original = nome
nome = nome.strip() # remove espaço em branco
print('Seu nome em letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas: {}'.format(nome.lower()))

# conta caractere eliminado espaço em branco
print('Seu nome "{}" tem {} caracteres.'.format(nome, len(nome) - nome.count(' ')))

separa = nome.split() # transforma string em lista
print('Seu primeiro nome "{}" tem {} caracteres.'.format(separa[0], len(separa[0])))


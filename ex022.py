print('Bom dia!')
nome = input('Por favor digite seu nome completo: ')
original = nome
nome = nome.strip()
print('Seu nome em letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas: {}'.format(nome.lower()))
print('Seu nome "{}" tem {} caracteres.'.format(nome, len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome "{}" tem {} caracteres.'.format(separa[0], len(separa[0])))


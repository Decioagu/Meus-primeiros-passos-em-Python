nome = input('Digite seu nome: ')
nome = nome.strip() #ELIMINA ESPAÇO
nome = nome.lower() #MINUSCULO
nome = nome.split() #TRANSFORMA EM LISTA
x = ('decio' or 'décio' in nome[0])
if x == True:
    print('Décio!!! Você fez esta programação!')
else:
    print('Você não é o Décio')

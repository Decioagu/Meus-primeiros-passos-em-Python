nome = input('Digite seu nome: ')
nome = nome.strip()
nome = nome.lower()
x = ('decio' or 'décio' in nome)
if x:
    print('Oi Décio!!!')
else:
    print('Você não é o Décio.')
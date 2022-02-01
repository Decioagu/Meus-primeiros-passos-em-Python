print('='*29)
print(' CADASTRO EM UM DICIONÁRIO '.center(29, '='))
print('='*29)
lista = []
dicionario = {}
opcao = ''
soma = cont1 = cont2 = 0
print()
while opcao != 'N':
    dicionario['nome'] = input('Nome: ').strip().upper()
    while True:
        sexo = input('Sexo: [M/F] ').strip().upper()
        if sexo in 'MF':
            dicionario['sexo'] = sexo
            break
        else:
            print('Informação invalida!')
            print('Digite "M" para MASCULINO ou "F" para FEMININO.')
    while True:
        idade = input('Idade: ')
        if idade.isnumeric() == True:
            dicionario['idade'] = int(idade)
            break
        else:
            print('Caracter invalido!')
            print('Favor digite apenas caracteres númericos.')
    lista.append(dicionario.copy())
    while True:
        opcao = input('Você quer contunuar? [S/N] ').strip().upper()
        if opcao == 'N':
            break
        elif opcao == 'S':
            print()
            break
        else:
            print('Informação invalida!')
            print('Digite "S" para CONTINUAR ou "N" para FINALIZAR.')

for c in range(0, len(lista)):
    soma += lista[c]['idade']
    if lista[c]['sexo'] == 'F':
        cont1 += 1
media = soma/len(lista)

print()
if len(lista) == 1:
    print(f'A) Ao todo foi cadastrada {len(lista)} pessoa.')
    if media <= 1:
        print(f'B) Sua idade é de {media:.0f} ano.')
    else:
        print(f'B) Sua idade é de {media:.0f} anos.')
    if lista[0]['sexo'] == 'F':
        print(f'C) A mulhere cadastrada foi {lista[0]["nome"]}.')
    else:
        print(f'C) Não houve cadastramento de nunhuma mulher.')

else:
    print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
    if media <=1:
        print(f'B) A média das idades é de {media:.0f} ano.')
    else:
        print(f'B) A média das idades é de {media:.2f} anos.')
    if cont1 == 0:
        print(f'C) Não houve cadastramento de nunhuma mulher.')
    elif cont1 == 1:
        print(f'C) A mulhere cadastrada foi ', end='')
        for c in range(0, len(lista)):
            if lista[c]['sexo'] == 'F':
                print(f'{lista[c]["nome"]}.')
    else:
        print(f'C) As mulheres cadastradas foram ', end='')
        for c in range(0, len(lista)):
            if lista[c]['sexo'] == 'F':
                cont2 += 1
                print(lista[c]["nome"], end='')
                if cont2 == cont1:
                    print('.')
                elif cont2 == cont1 - 1:
                    print(' e ', end='')
                else:
                    print(', ', end='')
    print(f'D) A lista de pessoas que estâo acaima da idade média são: ', end='')
    for c in range(0, len(lista)):
        if lista[c]['idade'] > media:
            if c == 0:
                print()
            print(f'Nome = {lista[c]["nome"]}; Sexo = {lista[c]["sexo"]}; Idade = {lista[c]["idade"]}.')
    if media == 1:
        print('0')
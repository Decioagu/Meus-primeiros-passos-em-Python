import datetime
D = {}
hoje = datetime.date.today().year
print('='*39)
print(' CADASTRO DE DADOS EM UM DIOCIONÁRIO '.center(39, '='))
print('='*39)

D['nome'] = input('Nome: ').strip().upper()

while True:
    ano = input('Ano de nascimento: ').strip()
    if ano.isnumeric() == True:
        ano = int(ano)
        if ((ano - hoje)* -1) >= 12:
            D['ano'] = int(ano)
            break
        else:
            print('Data invalida!')
            print(f'Ano atual {hoje}.')
            print(f'Não é permitido cadastro de pessoas menor de 12 anos.')
            print(f'Data minima para cadastro ano de {hoje - 12}')
            print()
    else:
        print('Caractere invalido!')
        print('Favor digitar apenas valoes númericos inteiros.')
        print()

D['aponsentadoria'] = 65 - (hoje - D['ano'])

while True:
    carteira = input('Número da carteira de trabalho (0 para não tem): ').strip()
    if carteira.isnumeric() == True:
        D['carteira'] = int(carteira)
        break
    else:
        print('Caractere invalido!')
        print('Favor digitar apenas valoes númericos inteiros.')
        print()

if D['carteira'] != 0:
    while True:
        contrat = input('Ano de contratação: ').strip()
        if contrat.isnumeric() == True:
            contrat = int(contrat)
            if ((ano - contrat) * -1) >= 12:
                D['contrat'] = int(contrat)
                break
            else:
                print('É proibido trabalho de carteira assiana para menores de 12 anos.')
                print(f'Data minima de validação apartir do ano de {ano + 12}.')
                print()
        else:
            print('Caractere invalido!')
            print('Favor digitar apenas valoes númericos inteiros.')
            print()

    while True:
        salario = input('Salario: R$').strip()
        salario_x = salario
        if salario_x.count('.') <= 1:
            salario_x = salario.replace('.', '')
            if salario_x.isnumeric() == True:
                D['salario'] = float(salario)
                break
            else:
                print('Caractere invalido!')
                print('Favor digitar apenas valoes númericos inteiros.')
                print()
        else:
            print('Favor digitar apenas valores númeriro separa do por um unico ponto "." para valores decinais.')
            print()


    print('='*50)
    print('Cadastro:')
    print(f'Nome: {D["nome"]}.')
    print(f'Idade: {D["ano"]}.')
    print(f'Númeroda carteira de trabalho: {D["carteira"]}.')
    print(f'Ano de contratação: {D["contrat"]}.')
    print(f'Salário: R${D["salario"]}')
    if D['aponsentadoria'] > 0:
        print(f'Faltam {D["aponsentadoria"]} para aposentadoria.')
    else:
        print('Já pode se aposentar! ')
else:
    print('=' * 50)
    print('Cadastro:')
    print(f'Nome: {D["nome"]}.')
    print(f'Idade: {D["ano"]}.')
print()
print(D)

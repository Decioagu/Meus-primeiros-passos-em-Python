limpar = '\033[m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
cinza = '\033[37m'
vermelho_claro = '\033[91m'
verde_claro = '\033[92m'
amarelo_claro = '\033[93m'
azul_claro = '\033[94m'
rosa = '\033[95m'
ciano_claro = '\033[96m'
branco = '\033[97m'
sub = '\033[4m'
neg = '\033[1m'
inv = '\033[7m'

from time import sleep
idade = cont = mais18 = homem = mulher = mulhermenos20 = 0
sexo = opcao = ''

while opcao != 'N':
    cont +=1
    print(f'{ciano}={limpar}'*30)
    print('{}{}{}'.format(verde_claro,'{:=^40}',limpar).format(f'{ciano_claro}CADASTRO DA {cont}º PESSOA{verde_claro}'))
    print(f'{ciano}={limpar}'*30)
    print()

    idade = int(input('Idade: '))
    if idade >= 18:
        mais18 +=1

    sexo = input(f'Sexo [{azul}M{limpar}/{rosa}F{limpar}]:').strip().upper()
    while sexo not in 'MF':
        print(f'{vermelho_claro}Opção invalida!{limpar}')
        sleep(1)
        print()
        print(f'Digite "{azul}M{limpar}" para {azul}masculino{limpar} ou "{rosa}F{limpar}" para {rosa}feminino{limpar}.')
        sexo = input(f'Sexo [{azul}M{limpar}/{rosa}F{limpar}]:').strip().upper()
    if sexo == 'M':
        homem += 1
    if sexo == 'F':
        mulher += 1
        if idade < 20:
            mulhermenos20 += 1

    opcao = input(f'Você quer continuar [{amarelo_claro}S{limpar}/{amarelo_claro}N{limpar}]?').strip().upper()
    while not opcao in 'SN':
        print(f'{vermelho_claro}Opção invalida!{limpar}')
        sleep(1)
        print()
        print(f'Digite "{amarelo_claro}S{limpar}" para {amarelo_claro}Sim{limpar} ou "{amarelo_claro}N{limpar}" para {amarelo_claro}Não{limpar}.')
        opcao = input(f'Você quer continuar [{amarelo_claro}S{limpar}/{amarelo_claro}N{limpar}]?').strip().upper()
    print()

print(f'{ciano}={limpar}'*33)
if cont > 1:
    print(f'Total de pessoas casatradas {amarelo}{cont}{limpar}.')
else:
    print(f'Cadastrado apenas {amarelo}{cont}{limpar} pessoa.')

if homem > 1:
    print(f'Tem {amarelo}{homem}{limpar} homens cadastrados.')
else:
    print(f'Tem {amarelo}{homem}{limpar} homem cadastrado.')

if homem > 1:
    print(f'Tem {amarelo}{mulher}{limpar} mulheres cadastradas.')
else:
    print(f'Tem {amarelo}{mulher}{limpar} mulher cadastrada.')

if mais18 > 1:
    print(f'Tem {amarelo}{mais18}{limpar} pessoas com mais de 18 anos.')
else:
    print(f'Tem {amarelo}{mais18}{limpar} pessoa com mais de 18 anos.')

if mulhermenos20 > 1:
    print(f'Tem {amarelo}{mulhermenos20}{limpar} mulheres com menos de 20 anos.')
else:
    print(f'Tem {amarelo}{mulhermenos20}{limpar} mulher com menos de 20 anos.')
print(f'{ciano}={limpar}' * 33)

from datetime import datetime


def titulo(txt):
    print(f'=' * (len(txt) + 4))
    print(f'= {txt} =')
    print(f'=' * (len(txt) + 4))


def teste_int(num):
    teste = num
    while True:
        if teste.count('-') == 1:
            teste = teste.replace('-', '')
            if teste.isnumeric():
                print(f'Favor digitar apenas valores numéricos inteiros e positivo.')
                print()
            teste = input(f'Digite um valor NUMÉRICO INTEIRO: ').strip()
        else:
            if teste.isnumeric():
                num = int(teste)
                if num > datetime.today().year:
                    print(f'Data informada deve ser MENOR ou IGUAL ao ano atual {datetime.today().year}.')
                    print()
                else:
                    break
            else:
                print(f'Erro...')
                print(f'Favor digitar apenas valores numéricos inteiros.')
                print()
            teste = input(f'Digite um valor NUMÉRICO INTEIRO: ').strip()
    return num


def voto(ano):
    ano = datetime.today().year - nascimento
    return ano


# CORPO PRINCIPAL
titulo('Funções para votação'.upper())
nascimento = input(f'Em que ano você nasceu? ')
nascimento = teste_int(nascimento)
nascimento = voto(nascimento)
if nascimento <= 1:
    print(f'Com {nascimento} ano: ', end='')
else:
    print(f'Com {nascimento} anos: ', end='')
if nascimento < 16:
    print('VOTO NEGADO!')
elif 16 <= nascimento < 18 or nascimento > 65:
    print('VOTO OPCIONAL!')
else:
    print('VOTO OBRIGATÓRIO!')




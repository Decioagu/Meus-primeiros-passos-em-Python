import COR
from time import sleep

def menu1():
    print(f'{COR.ciano_claro}={COR.limpar}' * (33))
    print('{}{}{}'.format(COR.roxo, 'LISTA DE CADASTRO'.center(33), COR.limpar))
    print(f'{COR.ciano_claro}={COR.limpar}' * (33))



def menu2():
    print(f'{COR.ciano_claro}={COR.limpar}' * (33))
    print('{}{}{}'.format(COR.roxo, 'CADASTRO'.center(33), COR.limpar))
    print(f'{COR.ciano_claro}={COR.limpar}' * (33))




def menu3():
    print(f'{COR.ciano_claro}={COR.limpar}' * (33))
    print('{}{}{}'.format(COR.roxo, 'SAIR DO PROGRAMA'.center(33), COR.limpar))
    print(f'{COR.ciano_claro}={COR.limpar}' * (33))
    sleep(1)


def opcao(op):
    while True:
        menu = input(op).strip()
        if menu.isnumeric():
            menu = int(menu)
            if menu == 1:
                menu1()
                break
            elif menu == 2:
                menu2()
                break
            elif menu == 3:
                menu3()
                break
            else:
                print(f'{COR.ciano_claro}={COR.limpar}' * (33))
                print('{}{}{}'.format(COR.vermelho_claro, 'Opção invalida!'.center(33), COR.limpar))
                sleep(1)
                break
        else:
            print(f'{COR.ciano_claro}={COR.limpar}' * (33))
            print('{}{}{}'.format(COR.vermelho_claro,'ERRO...'.center(33),COR.limpar))
            sleep(1)
            break
    return menu


def leiaint(msg):
    """
    Testa caractere e permanece em loop infinito até usuário
    digitar um número inteiro de qualquer valor

    :param msg: Recebe mensagem para variável "num" que será testada
    :return: Retorna somente valores numéricos inteiros
    """
    while True:
        try:
            num = input(msg).strip()
            teste = int(num)
        except ValueError:
            print()
            print(f'Erro...')
            print(f'Caractere "{num}" não é valido.')
            continue
        return teste

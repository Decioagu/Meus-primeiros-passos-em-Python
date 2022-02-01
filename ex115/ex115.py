import COR
import MENU
import TITULO
import ARQUIVO
cont = 0

arq = 'cadastro.txt'

if not ARQUIVO.arquivoExiste(arq):
    ARQUIVO.arquivoCriar(arq)
    a = open(arq, 'at')
    a.write(f'beneficiários'.center(33).upper())
    a.write('\n')
    a.close()

TITULO.titulo(f'Tratamento de Erros em Python'.upper())
while True:
    print(f'{COR.ciano_claro}={COR.limpar}' * (33))
    print('{}{}{}'.format(COR.roxo,f'MENU PRINCIPAL'.center(33),COR.limpar))
    print(f'{COR.ciano_claro}={COR.limpar}' * (33))
    print(f'{COR.amarelo_claro}1{COR.limpar} - {COR.verde_claro}Ver pessoas cadastrada{COR.limpar}')
    print(f'{COR.amarelo_claro}2{COR.limpar} - {COR.verde_claro}Cadastrar novas pessoas{COR.limpar}')
    print(f'{COR.amarelo_claro}3{COR.limpar} - {COR.verde_claro}Sair do sistema{COR.limpar}')
    print(f'{COR.ciano_claro}={COR.limpar}' * (33))
    menu = MENU.opcao(f'{COR.amarelo_claro}Digite a Opção:{COR.limpar} ')
    if menu == 1:
        if cont < 1:
            print()
        else:
            ARQUIVO.arquivoLer(arq)
    if menu == 2:
        cont += 1
        nome = input('Nome: ').upper()
        idade = MENU.leiaint('Idade: ')
        ARQUIVO.arquivoCadartrar(arq, nome, idade)
    if menu == 3:
        break



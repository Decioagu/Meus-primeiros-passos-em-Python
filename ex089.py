# TABELA DE CORES
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
# FIM DA TABELA DE CORES

print(f'{azul_claro}={limpar}'*32)
print(f'{azul_claro}={verde_claro} BOLETIM COM LISTAS COMPOSTAS {azul_claro}={limpar}')
print(f'{azul_claro}={limpar}'*32)
#print(len('Boletim com listas compostas')+4)

cadastro = []
alunos = []
cont = 0
opcao = ''

print()
while opcao != 'N':
    cont += 1
    print('{}{}{}'.format(f'{azul_claro}='*5, f' {verde_claro}CADASTRO DA {cont}ª PESSOA ', f'{azul_claro}={limpar}'*5))
    nome = input('Nome: ').strip().upper()
    alunos.append(nome)
    for n in range(1, 3):
        while True:
            nota = input(f'Nota {amarelo_claro}{n}{limpar}: ').strip()
            nota_x = nota
            if nota_x.count('.') <= 1:
                nota_x = nota_x.replace('.', '')
                if nota_x.isnumeric() == True:
                    nota = float(nota)
                    alunos.append(nota)
                    break
                else:
                    print(f'{vermelho_claro}Caracter invaliso!{limpar}')
                    print(f'{amarelo_claro}Favor digitar apenas valores númericos separados por um unico {vermelho_claro}"{amarelo_claro}.{vermelho_claro}" {amarelo_claro}para valores decinamais.{limpar}')
            else:
                print(f'{amarelo_claro}Favor digitar apenas valores númericos separados por um unico {vermelho_claro}"{amarelo_claro}.{vermelho_claro}" {amarelo_claro}para valores decinamais.{limpar}')

    cadastro.append(alunos[:])
    alunos.clear()

    while True:
        opcao = input(f'Quer continuar? [{amarelo_claro}S{limpar}/{amarelo_claro}N{limpar}] ').upper()
        if opcao == 'S':
            print()
            break
        else:
            if opcao == 'N':
                print()
                break
            else:
                print(f'{vermelho_claro}Opção invalida!{limpar}')
                print(f'Digite "{amarelo_claro}S{limpar}" para {amarelo_claro}CONTINUAR{limpar} ou "{amarelo_claro}N{limpar}" para {amarelo_claro}SAIR{limpar}.')

opcao = ''
cont = 0

print(f'{amarelo_claro}Núm  {ciano_claro}Média\t{roxo}Nome{limpar}')
for c in cadastro:
    cont += 1
    media = (c[1]+c[2])/2
    print(f'{amarelo_claro}{cont}    {ciano_claro}{media:.2f}\t{roxo}{c[0]}{limpar}')

print()
while opcao != 'N':
    while True:
        aluno = input(f'Mostrar nota de aluno "{amarelo_claro}Núm{limpar}": ').strip()
        if aluno.isnumeric() == True:
            aluno = int(aluno)
            break
        else:
            print(f'{vermelho_claro}Caracter invaliso!{limpar}')
            print(f'{amarelo_claro}Favor digitar apenas valores númericos separados por um unico {vermelho_claro}"{amarelo_claro}.{vermelho_claro}" {amarelo_claro}para valores decinamais.{limpar}')

    if 0 < aluno <= cont:
        print(f'Notas de {roxo}{cadastro[aluno-1][0]}{limpar} são {ciano_claro}{cadastro[aluno-1][1]}{limpar} e {ciano_claro}{cadastro[aluno-1][2]}{limpar}' )
    else:
        print(f'"{amarelo_claro}Núm{limpar}" {vermelho_claro}de aluno NÃO encotrado no cadastro!{limpar}')

    while True:
        opcao = input(f'Quer continuar? [{amarelo_claro}S{limpar}/{amarelo_claro}N{limpar}] ').upper()
        if opcao == 'S':
            print()
            break
        else:
            if opcao == 'N':
                print()
                break
            else:
                print(f'{vermelho_claro}Opção invalida!{limpar}')
                print(f'Digite "{amarelo_claro}S{limpar}" para {amarelo_claro}CONTINUAR{limpar} ou "{amarelo_claro}N{limpar}" para {amarelo_claro}SAIR{limpar}.')

print(f'{vermelho_claro}Fim do programa...{limpar}')

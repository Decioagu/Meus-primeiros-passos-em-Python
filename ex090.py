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

print(f'{azul_claro}={limpar}'*14)
print(f'{azul_claro}={verde_claro} DICIONÁRIO {azul_claro}={limpar}')
print(f'{azul_claro}={limpar}'*14)
#print(len('DICIONÁRIO')+4)

print()
aluno = dict()
aluno['nome'] = input('Nome: ').strip().upper()

while True:
    aluno['media'] = input(f'Média do {aluno["nome"]}: ').strip()
    teste = aluno['media']
    if teste.count('.') <= 1:
        teste = teste.replace('.', '')
        if teste.isnumeric() == True:
            aluno['media'] = float(aluno['media'])
            break
        else:
            print(f'{vermelho_claro}Caracter invaliso!{limpar}')
            print(f'{amarelo_claro}Favor digitar apenas valores númericos separados por um unico {vermelho_claro}"{amarelo_claro}.{vermelho_claro}" {amarelo_claro}para valores decinamais.{limpar}')
    else:
        print(f'{amarelo_claro}Favor digitar apenas valores númericos separados por um unico {vermelho_claro}"{amarelo_claro}.{vermelho_claro}" {amarelo_claro}para valores decinamais.{limpar}')

print()
print('='*40)
print(f'O nome do(a) aluno(a) é {azul_claro}{aluno["nome"]}{limpar}.')

print(f'A média de {azul_claro}{aluno["nome"]}{limpar} foi ', end='')
if aluno['media'] < 5:
    print(f'{vermelho_claro}{aluno["media"]:.2f}{limpar}')
elif aluno['media'] >= 7:
    print(f'{verde_claro}{aluno["media"]:.2f}{limpar}')
else:
    print(f'{amarelo_claro}{aluno["media"]:.2f}{limpar}')

print(f'Aluno(a) esta ', end='')
if aluno['media'] < 5:
    print(f'{vermelho_claro}REPROVADO(A)!{limpar}')
elif aluno['media'] >= 7:
    print(f'{verde_claro}APROVADO(A)!{limpar}')
else:
    print(f'em {amarelo_claro}RECUPERAÇÃO!{limpar}')
print('='*40)
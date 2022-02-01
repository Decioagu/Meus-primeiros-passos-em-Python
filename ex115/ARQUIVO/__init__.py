def arquivoExiste(pessoa):
    try:
        a = open(pessoa, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def arquivoCriar(pessoa):
    try:
        a = open(pessoa, 'wt+')
        a.close()
    except NameError:
        print('Houve problema em criar o arquivo')
    else:
        print(f'Arquivo criado {pessoa}')


def arquivoLer(pessoa):
    try:
        a = open(pessoa, 'rt')
    except NameError:
        print('Erro ao abrir o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def arquivoCadartrar(pessoa, nome='desconhecido', idade='descomnecido'):
    try:
        a = open(pessoa, 'at')
    except NameError:
        print('Erro de cadastro!')
    else:
        try:
            a.write('{: <35} {}\n'.format(f'Nome:{nome}', f'Idade:{idade}'.strip()))
        except:
            print('Erro de adição ao cadastro!')
        else:
            print(f'Cadastro de {nome} realizada com sucesso!')
    finally:
        a.close()


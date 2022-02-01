def notas(* num, sit=False):
    """
    A função notas calcula a média do aluno independente de quantas notas
    forem adicionado a média e possui o opcional da situação do aluno
    conforme valor da média >= 7 ou menor que 5.

    :param num: valores (notas) para calcular a média do aluno
    :param sit:(opcional) quanto a situação do aluno
    :return: retorna a um dicionario os parâmetros =>
    => Total: quantidade de notas inseridas;
    => Maior: maior nota;
    => Média: média entre as notas;
    => Situação: (opcional) se aluno foi ou não aprovado.
    """
    dic = {}
    dic['Total'] = len(num)
    dic['Maior'] = max(num)
    dic['Menor'] = min(num)
    dic['Média'] = sum(num)/len(num)
    if sit:
        if dic['Média'] >= 7:
            dic['Situação'] = 'APROVADDO'
        elif dic['Média'] < 5:
            dic['Situação'] = 'REPROVADO'
        else:
            dic['Situação'] = 'RECUPERAÇÃO'
    return dic

#__main__
resp = notas(7, 4, 5, 5, sit=True)
print(resp)
print()
help(notas)

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
    cont = len(num)
    maior = max(num)
    menor = min(num)
    media = sum(num)/cont
    if sit:
        if media >= 7:
            s = 'APROVADDO'
        elif media < 5:
            s = 'REPROVADO'
        else:
            s = 'RECUPERAÇÃO'
        dic = dict(Total=cont, Maior=maior, Menor=menor, Média=media, Situação=s)
    else:
        dic = dict(Total=cont, Maior=maior, Menor=menor, Média=media)
    return dic

#__main__
resp = notas(7, 9, 8, 5, sit=True)
print(resp)
print()
help(notas)

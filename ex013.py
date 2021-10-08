# Reajuste Salarial
print('Maria, vai haver um aumento e 15% nos salários!')
salario = float(input('Quanto você ganha mesmo? R$:'))
aumento = salario+((salario/100)*15)
print('Então agora você vai ganhar mais R$:{:.2f}, seu salário'
      ' vai para R$:{:.2f}'.format(((salario/100)*15), aumento))

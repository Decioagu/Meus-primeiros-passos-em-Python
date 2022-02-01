salario = float(input('Qual o salário do funcionário? '))
if salario > 1250:
    print('Terá um aumento de 10%.')
    print('Seu salário será R${:.2f}'.format(salario * 10 / 100 + salario))
else:
    print('Terá um aumento de 15%.')
    print('Seu salário será R${:.2f}'.format(salario * 15 / 100 + salario))

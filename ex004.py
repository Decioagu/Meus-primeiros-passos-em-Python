# Analise de variável tipo string => "x"
x = input('Digite algo: ')
print('O que foi digitado é do tipo:',type(x))
print('É um espaço em branco?',x.isspace())
print('É do tipo numérico?',x.isnumeric())
print('É do tipo alfabético?',x.isalpha())
print('É do tipo alfanumérico?',x.isalnum())
print('Tem somente letra maiúscula?',x.isupper())
print('Tem somente letra minuscula?',x.islower())
print('Possui a primeira letras maiúsculas e o restante minuscula?',x.istitle())
print('É do tipo decimal?',x.isdigit())


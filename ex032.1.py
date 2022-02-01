import datetime
print('Digite o ano de alguma data e veja se foi ou sera um ano bissexto.')
print('Caso queira ver o ano atual digite 0')
ano = int(input('Digite alguma data: '))


if ano == 0:
    ano = datetime.date.today().year
    print('Hoje é',ano)
if ano < 0:
    print('Data invalida, não existe ano menor que 1.')
elif 0 < ano < 1582:
    print('Calendário Gregoriano só iniciou apos 1582')
elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Este ano é bissexto!')
else:
    print('Este ano não é bissexto!')
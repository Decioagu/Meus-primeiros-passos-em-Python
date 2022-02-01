import datetime
print('Digite o ano de alguma data e veja se foi ou sera um ano bissexto.')
print('Caso queira ver o ano atual digite 0')
ano = int(input('Digite o ano: '))

if ano == 0:
    ano = datetime.date.today().year
    print('Hoje é', ano)
if 0 < ano < 1582:
    print('Calendário Gregoriano só iniciou apos 1582')
elif 1582 <= ano:
    if ano % 4 != 0:
        print('Ano comum')
    elif ano % 100 != 0:
        print('Ano bissexto')
    elif ano % 400 != 0:
        print('Ano comum')
    else:
        print('Ano bissexto')
else:
    print('Data invalida, não existe ano menor que 1.')
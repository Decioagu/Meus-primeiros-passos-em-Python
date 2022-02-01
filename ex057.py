limpa = '\033[m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
cinza = '\033[37m'
neg = '\033[1m'
sub = '\033[4m'
inv = '\033[7m'

print('{1}Digite o sexo da pessoa:{0}'.upper().format(limpa, amarelo))
sexo = input('SEXO [{1}M{0}/{2}F{0}]: '.format(limpa, azul, roxo, amarelo)).strip().upper()[0]
while sexo not in 'MF':
    print('{5}Opção invalida{0}, digite {1}"{4}M{0}{1}"{0} para {1}{3}masculino{0} e {2}"{4}F{0}{2}"{0} para '
          '{2}{3}feminino{0}.'.format(limpa, azul, roxo, sub, neg, vermelho))
    sexo = input('SEXO [{1}M{0}/{2}F{0}]: '.format(limpa, azul, roxo)).strip().upper()[0]
if sexo == 'M':
    print('{1}Masculino...{0}'.upper().format(limpa, azul))
else:
    print('{1}Feminino...{0}'.upper().format(limpa, roxo))
# Class polimorfismo

class Passaro:
    def voar(self):  # método voar
        print('Esta voando ^v^ !!!')

class Pardal(Passaro):
    def voar(self):  # método voar
        super(Pardal, self).voar()

class Avestruz(Passaro):
    def voar(self):  # método voar
        print('Avestruz não pode voar...')

def plano_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()
plano_voo(p1)
plano_voo(p2)

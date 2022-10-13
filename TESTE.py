class Bicicleta:
    # construtor
    def __init__(self, modelo, cor, ano, valor):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor

    # método
    def buzina(self):
        print('Plim, plim...')

    # método
    def andar(self):
        print('Pedalando!')

    # método
    def pare(self):
        print('Pare...')

    # método - 01 função __str__():
    #def __str__(self):
    #    return f'Classe Bicicleta: Modelo={self.modelo}, Cor={self.cor}, ano={self.ano}, Valor={self.valor}'

    # método - 02 função __str__():
    def __str__(self):
        return f'Classe {self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}'

b1 = Bicicleta('Caloi', 'Azul', 2018, 'R$:980,00')
b2 = Bicicleta('Montombike', 'Preta', 2020, 'R$:2000,00')

print(b1.modelo,b1.cor)  # ler objeto classe
b1.cor = 'Amarela' # alterar valor objeto classe
print(b1.modelo,b1.cor) # ler objeto classe
print(b2.modelo,b2.cor) # ler objeto classe
b1.buzina() # acesso ao método
Bicicleta.buzina(b1)  # acesso ao método
print(b2) # ler objeto classe __str__ caso haja


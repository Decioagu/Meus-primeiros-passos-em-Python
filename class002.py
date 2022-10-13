# Herança em Class

#Class Pai
class Veiculo:
    # construtor
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    # método
    def ligar_motor(self):
        print('Motor ligado!!!')

    # método - função string
    def __str__(self):
        return f'Classe {self.__class__.__name__}: {", ".join([f"{chave}:({valor})" for chave, valor in self.__dict__.items()])}.'

# Class Filho
class Moto(Veiculo):
    # construtor
    def __init__(self, cor, placa, numero_rodas, farol_esta_aceso=0):
        super(Moto, self).__init__(cor, placa, numero_rodas)  # Herança Class PAi
        self.farol_esta_aceso = farol_esta_aceso

    # método
    def farol_aceso(self):
        print(f'Farol {"esta" if self.farol_esta_aceso else "não esta"} aceso!!!')

# Class Filho
class Carro(Veiculo):
    # construtor
    def __init__(self, cor, placa, numero_rodas, passageiro=0):
        super(Carro, self).__init__(cor, placa, numero_rodas)  # Herança Class PAi
        self.passageiro = passageiro

    # método
    def tem_passageiro(self):
        print(f'{"Tem" if self.passageiro else "Não tem"} passageiro no carro!!!')

# Class Filho
class Caminhao(Veiculo):
    # construtor
    def __init__(self, cor, placa, numero_rodas, carregado=0):
        super().__init__(cor, placa, numero_rodas)  # Herança Class PAi
        self.carregado = carregado

    # método
    def esta_carregado(self):
        print(f'{"Sim" if self.carregado else "Não"} esta carregado!!!')


moto = Moto('Preta', 'ABC-1234', 2)  # inserir na Class
print('\n', moto)   # acesso método "string" Class Pai
moto.ligar_motor()  # acesso método Class Pai
moto.farol_aceso()  # acesso método Class Filho

carro = Carro('Branco', 'XYZ-1357', 4, 2)  # inserir na Class
print('\n', carro)  # acesso método "string" Class Pai
carro.ligar_motor()  # acesso método Class Pai
carro.tem_passageiro()  # acesso método Class Filho

caminhao = Caminhao('Azul', 'DSA-2468', 6, 'cheio')  # inserir na Class
print('\n', caminhao)  # acesso método "string" Class Pai
caminhao.ligar_motor()  # acesso método Class Pai
caminhao.esta_carregado()  # acesso método Class Filho

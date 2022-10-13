import datetime
# Class
class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento  # "_ano_nascimento" indica que objeto é privado (underline)

    # propriedade
    @property
    def idade(self):
        ano_atual = datetime.date.today().year
        return ano_atual - self._ano_nascimento

    # método
    def get_idade(self):
        ano_atual = datetime.date.today().year
        return ano_atual - self._ano_nascimento


pessoa = Pessoa('Décio Santana de Aguiar', 1981)
print(f'\n{pessoa.nome} tem {pessoa.idade}')  # uso de propriedade para leitura de idade
print(f'\n{pessoa.nome} tem {pessoa.get_idade()}')  # uso de método para leitura de idade

# Herança multipla em Class

#Class Pai
class Animal:
    # construtor
    def __init__(self, sangue_quente, numero_patas=2):
        self.sangue_quente = sangue_quente
        self.numero_patas = numero_patas
    #  método
    def __str__(self):
        return f'Classe {self.__class__.__name__}: {", ".join([f"{chave}:({valor})" for chave, valor in self.__dict__.items()])}.'

# Class Filho
class Mamifero(Animal):
    # construtor
    def __init__(self, mama, **kwargs):
        super(Mamifero, self).__init__(**kwargs)  # Herança Class PAi
        self.mama = mama
    #  método
    def mama_filhote(self):
        print('Seus filhotes mamam!!')

# Class Filho
class Ave(Animal):
    # construtor
    def __init__(self, bota_ovo, **kwargs):
        super(Ave, self).__init__(**kwargs)  # Herança Class PAi
        self.bota_ovo = bota_ovo

    def ovo(self):
        print('Esta com ovo no ninho!!')


# Class Neto
class Cachorro(Mamifero):
    # construtor
    def __init__(self, sangue_quente, numero_patas, mama, lati=0):
        #  print(Cachorro.__mro__)  # mostra ordem de declaração dos objetos
        super(Cachorro, self).__init__(sangue_quente=sangue_quente, numero_patas=numero_patas, mama=mama)
        self.lati = lati

    def esta_latindo(self):
        print(f'O cachorro {"esta" if self.lati else "não esta"} latindo!')

# Class Neto
class Galinha(Ave):
    # construtor
    def __init__(self, sangue_quente, numero_patas, bota_ovo, cacareja=0):
        #  print(Galinha.__mro__)  # mostra ordem de declaração dos objetos
        super(Galinha, self).__init__(sangue_quente=sangue_quente, numero_patas=numero_patas, bota_ovo=bota_ovo)
        self.cacareja = cacareja

    def esta_cacarejando(self):
        print(f'A galinha {"esta" if self.cacareja else "não esta"} cacarejando!')

# Class Neto
class Ornitorrinco(Mamifero, Ave):
    # construtor
    def __init__(self, sangue_quente, numero_patas, bota_ovo, mama, nada):
        #  print(Ornitorrinco.__mro__)  # mostra ordem de declaração dos objetos
        super().__init__(sangue_quente=sangue_quente, numero_patas=numero_patas, bota_ovo=bota_ovo, mama=mama)
        self.nada = nada

    def esta_nadando(self):
        print(f'O ornitorrinco {"esta" if self.nada else "não esta"} nadando!!!')

cachorro = Cachorro(sangue_quente='Sim', numero_patas=4, mama='Sim')
print('\n', cachorro)
# cachorro.ovo() # método não pertence a Class Mamífero (erro)
cachorro.mama_filhote()
cachorro.esta_latindo()
cachorro.lati = 'Sim'  # alterar valor objeto classe
cachorro.esta_latindo()

galinha = Galinha(sangue_quente='Sim', numero_patas=2, bota_ovo='Sim', cacareja='Sim')
print('\n', galinha)
# galinha.mama_filhote() # método não pertence a Class Ave (erro)
galinha.ovo()
galinha.esta_cacarejando()


#ornitorrinco = Ornitorrinco(sangue_quente='Sim', numero_patas=4, bota_ovo='Sim', mama='Sim', nada='Sim')
ornitorrinco = Ornitorrinco('Sim', 4,'Sim','Sim','Sim')  # necessário saber ordem dos objetos
print('\n', ornitorrinco)
ornitorrinco.ovo()
ornitorrinco.mama_filhote()
ornitorrinco.esta_nadando()


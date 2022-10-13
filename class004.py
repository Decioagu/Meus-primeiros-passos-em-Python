# Classe objeto privado (encapsulamento) e propriedade

# Class
class Foo:
    def __init__(self, n=0):
        self._n = n  # "_n" indica que objeto é privado (underline)

    @property  # propriedade
    def n(self):
        return self._n or 0

    @n.setter  # propriedade
    def n(self, valor):
        _n = self._n or 0
        _valor = valor or 0
        self._n += _valor

    @n.deleter  # propriedade
    def n(self):
        #  self._n -= 1
        self._n = 0

foo = Foo(35)  # propriedade "@property"
print(foo.n)
foo.n = 15  # propriedade "@n.setter"
print(foo.n)
del foo.n  # propriedade "@n.deleter"
print(foo.n)

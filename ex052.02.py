n = int(input('Digite um número inteiro: '))
while n > 1:
        def div(x):
                cont = 2
                while x % cont != 0 and cont < x/2:
                        cont = cont+1
                if x % cont != 0 or x == 2:
                        return False
                else:
                        return True

        if div(n):
                print('Não é primo:',n)
                print()
        else:
                print('É primo:',n)
                print()
        n = int(input('Digite um número inteiro: '))

print("Número inteiro igual ou menor que 1, não são primo.") 

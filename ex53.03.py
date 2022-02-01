text = input("Digite um texto:")

# Remove os espaços
text = text.replace(' ','')

# texto deve ser maior que um e texto deve ser igual ao seu oposto
if len(text) > 1 and text.upper() == text[::-1].upper():
	print('Seu texto É um PALINDROMO!')
	print(f'{text} = {text[::-1]}')
else:
	print('Seu texto é  NÃO um PALINDROMO!')
	print(f'{text} ≠ {text[::-1]}')
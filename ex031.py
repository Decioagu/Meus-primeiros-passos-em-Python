km = int(input('Por favor, informe quantos Km você vai viajar: '))
if km <= 200:
    print('Uma viagem de {}Km, vai custar R${:.2f}'.format(km, km * 0.5))
else:
    print('Uma viagem de {}Km, vai custar R${:.2f}'.format(km, km * 0.45))


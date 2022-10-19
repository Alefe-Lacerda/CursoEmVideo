distancia = int(input('Distância: '))

if distancia > 200:
    preco = 0.45 * distancia
else:
    preco = 0.5 * distancia

print('O preço de sua viagem é de R${:.2f}'.format(preco))

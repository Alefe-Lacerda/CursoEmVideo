# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = int(input('Distância: '))

if distancia > 200:
    preco = 0.45 * distancia
else:
    preco = 0.5 * distancia

print('O preço de sua viagem é de R${:.2f}'.format(preco))

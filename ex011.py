largura = float(input('Digite a largura em metros:'))
altura = float(input('Digite a altura em metros:'))
area = largura * altura
litros = area / 2

print('São necessário {} litros de tinta, pois a parede tem {}m²'.format(litros,area))
km = float(input('Kilômetros rodados: '))
dias = int(input('Dias alugados: '))
custo_por_km = km * 0.15
custo_por_dia = dias * 60
preco_total = custo_por_dia + custo_por_km
print('Preço por dia: R${:.2f}'.format(60))
print('Preço por kilômetros rodados: R${:.2f}'.format(0.15))
print('Total a pagar: R${:.2f}'.format(preco_total))
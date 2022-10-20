# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Kilômetros rodados: '))
dias = int(input('Dias alugados: '))
custo_por_km = km * 0.15
custo_por_dia = dias * 60
preco_total = custo_por_dia + custo_por_km
print('Preço por dia: R${:.2f}'.format(60))
print('Preço por kilômetros rodados: R${:.2f}'.format(0.15))
print('Total a pagar: R${:.2f}'.format(preco_total))

# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Ano: '))

if ano % 4 == 0:
    print('É bissexto.')
else:
    print('Não é bissexto.')

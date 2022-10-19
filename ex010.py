real = float(input('Digite quanto vc tem: R$'))
dolar = real / 5.09
euro = real / 5.39
libra = real / 6.28

print('Vc pode comprar US${:.2f}, €{:.2f} e £{:.2f}'.format(dolar, euro, libra))
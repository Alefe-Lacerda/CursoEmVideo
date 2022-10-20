# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metro = float(input('Insira a medida em metros:'))
centimetro = metro * 100
milimetro = metro * 1000
print('A medida contém {} cm'.format(centimetro))
print('A medida contém {} mm'.format(milimetro))

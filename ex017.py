# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
c_o = float(input('Cateto oposto: '))
c_a = float(input('Cateto adjacente: '))
hipotenusa = hypot(c_o, c_a)
print('Hipotenusa: {}'.format(hipotenusa))

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
angulo = float(input('Ângulo: '))
rad = radians(angulo)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)

print('Seno: {}'.format(seno))
print('Cosseno: {}'.format(cosseno))
print('Tangente: {}'.format(tangente))

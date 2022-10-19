from math import hypot
c_o = float(input('Cateto oposto: '))
c_a = float(input('Cateto adjacente: '))
hipotenusa = hypot(c_o, c_a)
print('Hipotenusa: {}'.format(hipotenusa))
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float(input('Reta A: '))
b = float(input('Reta B: '))
c = float(input('Reta C: '))

if a + b > c and a + c > b and b + c > a:
    print('É possível fazer um triângulo com essas 3 retas.')
else:
    print('Não é possível fazer um triângulo com essas 3 retas.')

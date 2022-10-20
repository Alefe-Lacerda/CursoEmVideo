# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Com strings

# numero = input('Número de 0 a 9999: ')
# unidade = numero[3]
# dezena = numero[2]
# centena = numero[1]
# milhar = numero[0]
#
# print('Unidade: {}'.format(unidade))
# print('Dezena: {}'.format(dezena))
# print('Centena: {}'.format(centena))
# print('Milhar: {}'.format(milhar))


# Com números

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar:{}'.format(m))

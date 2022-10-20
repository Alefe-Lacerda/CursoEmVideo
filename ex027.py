# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Seu nome completo: ')).split()
primeiro = nome[0]
ultimo = nome.pop()
print('Primeiro nome: ', primeiro)
print('Último nome: ', ultimo)

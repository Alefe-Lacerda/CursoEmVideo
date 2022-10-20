# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# -> O nome com todas as letras maiúsculas e minúsculas.
# -> Quantas letras ao todo (sem considerar espaços).
# -> Quantas letras tem o primeiro nome.
nome_completo = str(input('Seu nome completo: '))
minusculas = nome_completo.lower()
maiusculas = nome_completo.upper()
numero_de_letras = len(nome_completo.replace(" ", ""))
divisao_nome = nome_completo.split()

print('Seu nome completo mainúsculo: {}'.format(minusculas))
print('Seu nome completo maiúsculo: {}'.format(maiusculas))
print('Número de letras do seu nome: {}'.format(numero_de_letras))
print('Primeiro nome: {}'.format(divisao_nome[0].title()))
print('Número de letras do primeiro nome: {}'.format(len(divisao_nome[0])))

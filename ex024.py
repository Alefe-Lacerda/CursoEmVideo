# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = input('Cidade: ').strip().upper()
print('SANTO' in cidade[:5])

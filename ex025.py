# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Nome: ').title()
print('Contém Silva no seu nome?')
if ('Silva' in nome) == True:
    print('Sim')
else:
    print('Não')

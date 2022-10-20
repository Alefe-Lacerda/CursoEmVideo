# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
funcionario = input('Nome do Funcionário: ')
salario = float(input('Salário de {}: R$'.format(funcionario)))
novoSalario = salario + (salario* 15/100)
print('O novo saláio de {}, com 15% de aumento, é {:.2f}R$'.format(funcionario, novoSalario))

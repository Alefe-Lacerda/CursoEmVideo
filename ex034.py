# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Salário atual: '))

if salario > 1250:
    salario_novo = salario + (salario * 0.10)
else:
    salario_novo = salario + (salario * 0.15)

print('Salário Novo: {}'.format(salario_novo))

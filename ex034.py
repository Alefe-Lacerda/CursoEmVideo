salario = float(input('Salário atual: '))

if salario > 1250:
    salario_novo = salario + (salario * 0.10)
else:
    salario_novo = salario + (salario * 0.15)

print('Salário Novo: {}'.format(salario_novo))
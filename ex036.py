# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# Calcule o valor da prestação mensal.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_da_casa = float(input('Valor da casa: '))
salario_do_comprador = float(input('Salário do comprador: '))
anos_pagamento = int(input('Em quantos anos irá pagar: '))

prestacao_mensal = valor_da_casa / (12 * anos_pagamento)
porcentagem_salario = (prestacao_mensal/salario_do_comprador)*100
print('Sua prestação mensal é: {:.2f}, {:.2f}% do salário'.format(prestacao_mensal, porcentagem_salario))

if porcentagem_salario > 30:
    print('Empréstimo recusado pois o valor excede a 30% do seu salário.')
else:
    print('Empréstimo aceito, compre sua casinha e seja feliz :) ')

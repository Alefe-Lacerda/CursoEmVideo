velocidade = int(input('Digite a velocidade por hora: '))
velocidade_maxima = 80

if velocidade > velocidade_maxima:
    valor_da_multa = (velocidade - velocidade_maxima) * 7
    print('Vc foi multado e sua multa é de R${:.2f}'.format(valor_da_multa))

print('Tenha um ótimo dia :)')

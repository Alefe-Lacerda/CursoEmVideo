# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input('Digite a velocidade por hora: '))
velocidade_maxima = 80

if velocidade > velocidade_maxima:
    valor_da_multa = (velocidade - velocidade_maxima) * 7
    print('Vc foi multado e sua multa é de R${:.2f}'.format(valor_da_multa))

print('Tenha um ótimo dia :)')

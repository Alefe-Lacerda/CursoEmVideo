frase = input('Diga sua frase: ').strip()
numero_de_vezes = frase.upper().count('A')
primeira_vez = frase.upper().find('A')
ultima_vez = frase.upper().rfind('A')

print('Quantas vezes aparece o "A": {}'.format(numero_de_vezes))
print('Posição que aparece o "A" pela primeira vez: {}'.format(primeira_vez))
print('Posição que aparece o "A" pela última vez: {}'.format(ultima_vez))

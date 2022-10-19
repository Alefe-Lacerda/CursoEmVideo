from random import choice

print('Bem vindo ao joguin!')
numeros = [0, 1, 2, 3, 4, 5]
numero_escolhido_pelo_pc = choice(numeros)
tentativa = int(input('Um número entre 0 e 5: '))

if tentativa == numero_escolhido_pelo_pc:
    print('Você ganhou, parabéns!')
else:
    print('Você perdeu, o número era o {}, seu cocô!'.format(numero_escolhido_pelo_pc))
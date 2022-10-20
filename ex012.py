# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Preço do produto: R$'))
novoPreco = preco - (preco * 5/100)
print('Novo preço com 5% de desconto: R${:.2f}'.format(novoPreco))

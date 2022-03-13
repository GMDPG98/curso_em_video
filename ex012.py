# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: R$ '))
desconto = preco - (preco * 0.05)

print('O valor do produto com desconto será de R$ {:.2f} Reais'.format(desconto))

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos Dólares ela pode comprar.

carteira = float(input('Quanto dinheiro você têm? '))
dolares = carteira / 5.65

print('Com {} Reais você consegue comprar {:.2f} Dólares'.format(carteira, dolares))

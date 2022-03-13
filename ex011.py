# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua
# área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta,
# pinta uma área de 2m².

altura = float(input('Qual é a altura da parede? '))
largura = float(input('Qual é a largura da parede? '))
area = altura * largura
tinta = area / 2

print('Será necessário {} litros de tinta, para pintar a parede de {} m²'.format(tinta, area))

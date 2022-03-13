# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

cateto1 = float(input('Digite o valor do cateto oposto do triângulo: '))
cateto2 = float(input('Digite o valor do cateto adjacente do triângulo: '))
print('A hipotenusa do triângulo é igual à {:.2f}'.format(hypot(cateto1, cateto2)))

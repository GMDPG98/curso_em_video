# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse ângulo.

from math import cos, sin, tan, radians

angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo {}º tem seu seno valendo {:.2f}, cosseno valendo {:.2f} e tangente valendo {:.2f}'.format(angulo, seno, cosseno, tangente))

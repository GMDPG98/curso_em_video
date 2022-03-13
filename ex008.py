# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros
# e milímetros.

distancia = float(input('Digite o valor da distância: '))
centimetros = distancia * 100
milimetros = distancia * 1000

print('O valor {} metros corresponde à {} centímetros e {} milímetros'.format(distancia, centimetros, milimetros))

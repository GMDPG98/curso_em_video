# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu
# antecessor

numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1

print('O antecessor de {} é igual à {} e o sucessor é igual à {}'.format(numero, antecessor, sucessor))

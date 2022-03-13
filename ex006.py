# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1 / 2)

print(
    'O dobro de {} é igual à {}, o triplo é igual à {} e a raiz quadrada é igual à {:.2f}'.format(numero, dobro, triplo,
                                                                                                  raiz))

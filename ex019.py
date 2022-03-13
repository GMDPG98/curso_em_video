# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
# ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

primeiro = input('Digite o nome: ')
segundo = input('Digite o nome: ')
terceiro = input('Digite o nome: ')
quarto = input('Digite o nome: ')

print('O aluno escolhido foi o/a {}'.format(choice([primeiro, segundo, terceiro, quarto])))

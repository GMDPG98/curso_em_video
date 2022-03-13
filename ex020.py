# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample

primeiro = input('Digite o nome: ')
segundo = input('Digite o nome: ')
terceiro = input('Digite o nome: ')
quarto = input('Digite o nome: ')

print('A ordem dos alunos para apresentar o trabalho será {}'.format(sample([primeiro, segundo, terceiro, quarto], k=4)))

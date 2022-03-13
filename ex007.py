# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input('Digite o nome do aluno: ')
primeiraNota = float(input('Digite a primeira nota: '))
segundaNota = float(input('Digite a segunda nota: '))
media = (primeiraNota + segundaNota) / 2

print('A media do aluno {} vai ser igual à {}'.format(nome, media))

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de
# aumento.

nome = input('Qual é o nome do funcionário? ')
salario = float(input('Digite o salário do funcionário: R$ '))
aumento = salario + (salario * 0.15)

print('O salário do funcionário {} será de R$ {:.2f} Reais'.format(nome, aumento))

distancia = float(input('Qual foi a km percorrida? '))
dias = int(input('Quantos dias de aluguél? '))
preco = (dias * 60) + (distancia * 0.15)

print('O preço final a pagar pelo aluguel foi de R$ {}'.format(preco))
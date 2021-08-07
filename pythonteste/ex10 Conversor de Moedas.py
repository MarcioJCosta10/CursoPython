din = float(input('Quantos dinheiro você tem na carteira? R$  '))
dolar = 5.12
conv = din / dolar
print('Com R$ {:.2f} você pode comprar U$${:.0f} dolares '.format(din,conv))
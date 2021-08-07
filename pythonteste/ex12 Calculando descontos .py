preco = float(input('Qual é o preço do produto:R$ '))
desconto = float(input('Quantos % será de desconto?: ' ))
desc = desconto / 100
novo_preco = preco - (preco * desc)
print('O que custava R$ {:.2f} na promoção vai custar  R$ {:.2f}'.format(preco, novo_preco))
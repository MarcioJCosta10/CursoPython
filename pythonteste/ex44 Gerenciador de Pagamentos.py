print('{:=^40}'.format(" LOJA GUANABARA "))
nome = str(input('\033[33m'"Digite o nome do produto: "'\033[33m'))
produto = float(input("Informe o preço do produto: R$ "))
print(''' FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2 x no cartão
[4] 3 x ou mais no cartão ''')
condicao = int(input("Qual é a opção?: "))
if condicao == 1:
    print("O valor do produto {} com o desconto será de R$ {:.2f} ".format(nome, produto - (produto * 0.40)))
elif condicao == 2:
    print("O valor do produto {} com o desconto será de R$ {:.2f} ".format(nome, produto - (produto * 0.30)))
elif condicao == 3:
    total = produto
    parcela = total / 2
    print("Sua compra do produto {} será parcelada em 2 x de R$ {:.2f} SEM JUROS ".format(nome, parcela))
elif condicao ==4:
    total = produto + (produto * 20/100)
    totalpar = int(input("Quantas parcelas: "))
    parcela = total / totalpar
    print("Sua compra do produto {} será parcelada em {} x de R$ {:.2f} COM JUROS ".format(nome,totalpar, parcela))
else:
    print('\033[31m'"Opção Inválida tente Novamente"'\033[m')
    print("Condição de pagamento não é válida, então o valor será R$ {:.2f} à vista".format(produto))


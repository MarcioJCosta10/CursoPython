vc = float(input("Qual é o valor da casa: R$ "))
vs = float(input("Qual é o valor do salário: R$ "))
va = int(input("Em quantos anos você dejesa pagar a sua casa: "))
vp = vc / (va*12)
print("Para pagar uma casa de R${:.2f} em {} anos ".format(vc,va),end='')
print("a prestação será de R$ {:.2f}".format(vp))
if vp >= vs - (vs * 0.7):
    print("Emprestimo negado")
else:
    print("O valor da prestação é: {:.2f} ".format(vp))
    print("Emprestimo Aprovado")


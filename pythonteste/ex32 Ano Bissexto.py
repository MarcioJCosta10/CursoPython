from datetime import date
ano = int(input("Informe o ano que deseja consultar: Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é Bissesto".format(ano))
else:
    print('O ano {} não é bissesto'.format(ano))





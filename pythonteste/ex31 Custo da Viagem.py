distancia = float(input("Digite a distância da viagem em km: "))
valorkm200 = 0.50
valorkm201 = 0.45
if distancia < 200:
    print(" O valor da passagem será de R${:.2f}".format(distancia*valorkm200))
else:
    print(" O valor da passagem será de R${:.2f}".format(distancia * valorkm201))
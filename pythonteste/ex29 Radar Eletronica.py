velocidade = int(input("Informe a velicidade do veiculo: "))
print("A velocidade do veículo é {} km/h".format(velocidade))
vp = 80
if velocidade > 80:
    multa = (velocidade - vp)*7
    print("Você está acima da velocidade permitida, a sua multa será de R${:.2f}".format(multa))
else:
    print("A velocidade está normal, siga em frente!")
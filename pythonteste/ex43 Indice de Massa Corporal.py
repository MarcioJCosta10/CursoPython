import math
a = float(input("Informe sua altura: "))
p = float(input("Informe seu peso: "))
imc = p / math.pow(a, 2)
print("O IMC dessa pessoa é {:.2f} ".format(imc))
print("Com a altura {} e o peso {} seu IMC é {:.2f}".format(a, p, imc))
if imc <= 18.25:
    print("Você está abaixo do peso! ")
elif 18.25 <= imc <= 25:
    print("Seu peso está ideal! ")
elif 25 <= imc < 30:
    print("Você está com sobrepeso! " )
elif 30 <= imc < 40:
    print("Você está com obesidade! ")
elif imc >= 40:
    print("Você está com obesidade morbida, cuidado!")


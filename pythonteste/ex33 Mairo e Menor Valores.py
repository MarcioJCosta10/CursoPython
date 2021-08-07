num1= int(input("Digite o primeiro numero: "))
num2= int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
# Verificando qual é o menor
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3< num2:
    menor = num3
print("O menor numero é {} ".format(menor))
# Verificando qual é o maior
maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
print("O maior numero é {} ".format(maior))







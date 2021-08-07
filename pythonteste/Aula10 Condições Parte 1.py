nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print("A sua média foi {:.2f}".format(media))
print("Parabéns"if media >= 8 else "Reprovado")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print("Tirando {} e {} a sua média é {}".format(nota1,nota2,media))
print("A sua média é {}".format(media))
if media < 5:
    print("Você foi reprovado!")
elif media > 5 and media < 7:
    print("Você está de recuperação!")
else:
    print("Você está aprovado!")
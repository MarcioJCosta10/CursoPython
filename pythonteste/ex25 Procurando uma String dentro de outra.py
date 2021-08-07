nome = str(input("Digite o seu nome completo: ")).lower().strip()
print("O seu nome tem silva? {}".format('silva' in nome.lower().strip()))
lista = ["silva"]
if lista[0] in nome:
    print( " O seu nome contém Silva")
else:
    print("O seu nome não contém Silva")
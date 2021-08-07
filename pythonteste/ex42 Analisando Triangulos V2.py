print('\033[30;44m -= \033[m'*10)
print("Analizador de Triangulos")
print('\033[30;44m -= \033[m'*10)
r1 = float(input("Informe o 1 segmento: "))
r2 = float(input("Informe o 2 segmento: "))
r3 = float(input("Informe o 3 segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r2 < r1 + r2:
    print("Podemos formar um triangulo", end='')
    if r1 == r2 == r3:
        print(" Equilátero")
    elif r1 != r2 != r3 != r1:
        print(" Escaleno")
    else:
        print(" Isóceles")
else:
    print("Não podemos formar um triangulo")





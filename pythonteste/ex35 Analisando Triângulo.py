print('\033[7;30;44m -= \033[m'* 20)
print("Analizador de Triangulos")
print('\033[7;30;44m -= \033[m'*20)
r1 = float(input("Informe o 1 segmento"))
r2 = float(input("Informe o 2 segmento"))
r3 = float(input("Informe o 3 segmento"))
if r1 < r2 + r3 and r2 < r1 + r3 and r2 > r1 + r2:
    print("Podemos formar um triangulo")
else:
    print("Não podemos formar um trinagulo")

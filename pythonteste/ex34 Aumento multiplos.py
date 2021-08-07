salario = float(input("Informe seu salário: "))
if salario <= 1250.00:
    salario = salario + (salario*0.15)
    print("O valor do seu salário será R$ {:.2f} ".format(salario))
else:
    salario = salario + (salario*0.10)
    print("O valor do seu salário será R$ {:.2f} ".format(salario))
salario = float(input('Informe o valor do salário do funcionário:R$ '))
reajuste = float(input('Informe o % do reajuste: '))
valor_reajuste = reajuste / 100
novo_salario = salario + (salario * valor_reajuste)
print('Um funcionário que ganhava R$ {:.2f} com um aumento de {}%  passa a receber R$ {:.2f}'.format(salario, reajuste, novo_salario))

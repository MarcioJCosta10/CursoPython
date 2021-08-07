num = int(input("Digite um numero inteiro: "))
print('''Escolha uma das bases para a conversão:
      [1] Converter para BINÁRIO
      [2] Converter para HEXADECIMAL
      [3] Converter para OCTAL''' )
escolha = int(input("Digite a opção desejada: "))

if escolha == 1:
    print("{} convertido para BINÁRIO é {}".format( num, bin(num)[2:]))
elif escolha == 2:
    print("{} convertido para HEXADECIMAL é {}".format(num, hex(num)[2:]))
elif escolha == 3:
    print("{} convertido para OCTAL é {} ".format(num, oct(num)[2:]))
else:
    print("Escolha invalidade, tente novamente!")


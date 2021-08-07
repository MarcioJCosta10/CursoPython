nome = str(input("Qual é o seu nome? "))
if nome == "Gustavo":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Marcia" or nome == "Paulo":
    print('\033[34m',"O seu nome é bem comum no Brasil!",'\033[m')
elif nome in "Ana Claudia Jessica Juliana":
    print('\033[35m',"Belo nome feminino!",'\033[m')
else:
    print('\033[33m',"O seu nome é bem normal",'\033[m')
print('\033[32m',"Tenha um bom dia {}!".format(nome),'\033[m')
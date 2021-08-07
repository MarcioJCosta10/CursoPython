from datetime import date

data_atual = date.today().year
ano_nasc = int(input("Digite o seu ano de nascimento: "))
idade = data_atual - ano_nasc
print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    print("A sua categoria é"'\033[34m',"MIRIM",'\033[m')
elif idade <= 14:
    print("A sua categoria é"'\033[34m',"INFANTIL",'\033[m')
elif idade <= 19:
    print("A sua categoria é"'\033[34m',"JUNIOR",'\033[m')
else:
    print("A sua categoria é"'\033[34m',"MASTER",'\033[m')

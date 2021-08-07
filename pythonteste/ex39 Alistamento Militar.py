from datetime import date
atual = date.today().year
nascimento = int(input("Digite seu ano de nascimento: "))
sexo = str(input("Informe seu sexo: [H/M]").upper())
idade = atual - nascimento
if sexo == 'M':
    print("Você não precisa efetuar o alistamento Obrigatorio!")
    exit()
print("Quem nasceu em {} tem {} em {}.".format(nascimento, idade, atual))

if idade == 18:
    print("Voce tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
    saldo = 18 - idade
    print("Voce ainda não tem 18 anos ainda falta {} para o alistamento. ".format(saldo))
    print("Seu alistamento será em {}.".format(atual + saldo))

elif idade > 18:
    saldo = idade - 18
    print("Voce deveria ter se alistado a {} anos.".format(saldo))
    print("Seu alistamento deveria ter sido em {}.".format(atual - saldo))
























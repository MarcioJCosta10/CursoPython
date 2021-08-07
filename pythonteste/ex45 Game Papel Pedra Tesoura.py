from random import randint
from time import sleep

itens = ('pedra','papel','tesousa')
computador = randint(0,2)
print(''''Suas Opções
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input("Qual é a sua jogada: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
print("-="*13)
print("O computador jogou {}".format(itens[computador]))
print("O jogador jogou {}".format(itens[jogador]))
print("-="*13)
if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("Jogada Inválida")

elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("Jogada Inválida")

elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("Jogada Inválida")








"""import random
print(''' Suas opções de jogada:
 [1]Pedra
 [2]Papel
 [3]Tesousa''')
jogador= int(input("Digite sua opção de jogada: "))
print("JO")
print("KEN")
print("PO!!!")
print("-="*20)
computador= random.randint(1,3)
Pedra = "Pedra"
Papel = "Papel"
Tesoura = "Tesoura"

if jogador == 1 and computador==2:
    print("O jogador escolheu Pedra")
    print("O computador escolheu Papel")
    print("{} vence da {}".format(Papel , Pedra))
    print("O Computador venceu!")
elif jogador == 1 and computador ==3:
    print("O jogador escolheu Pedra")
    print("O computador escolheu Tesoura")
    print("{} vence da {}".format(Pedra,Tesoura))
    print("O Jogador venceu!")
elif jogador ==1 and computador ==1:
    print("O jogador escolheu Pedra")
    print("O computador escolheu Pedra")
    print("{} empata com {}".format(Pedra,Pedra))
    print("Houve um empate!")
elif jogador == 2 and computador == 1:
    print("O jogador escolheu Papel")
    print("O computador escolheu Pedra")
    print("{} vence da {}".format(Papel,Pedra))
    print("O Jogador venceu!")
elif jogador == 2 and computador == 3:
    print("O jogador escolheu Papel")
    print("O computador escolheu Tesoura")
    print("{} vence da {} ".format(Tesoura,Papel))
    print("O Computador venceu!")
elif jogador == 2 and computador == 2:
    print("O jogador escolheu Papel")
    print("O computador escolheu Papel")
    print("{} empata com {}".formt(Papel,Papel))
    print("Houve um empate!")
elif jogador == 3 and computador == 1:
    print("O jogador escolheu Tesoura")
    print("O computador escolheu Pedra")
    print("{} vence da {}".format(Pedra,Tesoura))
    print("O Computador venceu!")

elif jogador == 3 and computador == 2:
    print("O jogador escolheu Tesoura")
    print("O computador escolheu Papel")
    print("{} vence do {} ".format(Tesoura,Papel))
    print("O Jogador venceu!")
else:
    print("O jogador escolheu Tesousa")
    print("O computador escolheu Tesoura")
    print("{} empata com {} ".format(Tesoura,Tesoura))
    print("Houve um empate!")
print("-=" * 20)"""

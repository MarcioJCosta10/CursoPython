from random import randint
from time import sleep
num = randint(0,5) # faz o computar sorter
print('\033[34m',"-=-"*20,'\033[m')
print("Vou pensar em um número entre 0 e 5. Tente adivinhar... ")
print('\033[34m',"-=-"*20,'\033[m')

jogo = int(input("Em que numero eu pensei? "))# Jogador tenta adivinhar
print("Processando...")
sleep(3)
if jogo == num:
    print('\033[35m',"Parabéns! Você Veceu",'\033[m')
else:
    print('\033[36m',"Tente Novamente",'\033[m')
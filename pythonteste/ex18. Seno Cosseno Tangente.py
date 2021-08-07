import math
from math import tan, radians

'''Exercicio 18 faça um programa que leia um angulo e retorne seu seno cosseno e tangente

 Primeiro preciso converter para radianos e depois calcular '''

angulo = float(input("Digite o angulo que quer calcular: "))
sen = math.sin(math.radians(angulo)) # Usando com a importação da biblioteca math

print("O angulo de {:.2f} tem o seno de {:.2f}".format(angulo, sen))
coss = math.cos(math.radians(angulo)) # Usando com a importação da biblioteca math


print("O angulo de {:.2f} tem o cosseno de {:.2f}".format(angulo, coss))
tangente = tan(radians(angulo)) # Usando com importação especifica dos módulos

print("A tangente de {:.2f} é {:.2f}".format(angulo, tangente))


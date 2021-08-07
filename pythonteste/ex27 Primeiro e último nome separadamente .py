n = str(input("Digite o seu nome completo: ")).upper().strip()
print("Muito prazer em te conhecer!".format(n))

nome = n.split()
print("O seu primeiro nome é:{} ".format(nome[0]))
print("O seu último nome é:{}" .format(nome[len(nome)-1]))
# nome[len(nome)-1 Pega a ultima posição pois o tamanho da lista
# é igual ao seu ultimo elemento na lista e menos 1 é para tirar o 0



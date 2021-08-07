cores={'limpa':'\033[m',
       'Azul':'\033[34m',
       'Amarela':'\033[33m',
       'pretoebranco':'\033[7;30;'}
nome = str(input("Por favor, digite seu nome completo: "))
print("Analisando seu nome...")
print("Olá, seu nome em maiúsculo é", cores['Azul'],nome.upper(),cores['limpa'])
print("Olá seu nome em minúsculo é",cores['Amarela'], nome.lower(),cores['limpa'])
print("O nome sem espaços iniciais e finais tem {} letras".format(len(nome.strip())-nome.count(' ')))
print("O seu primeiro nome  tem {} letras".format(nome.find(' ')))
lista = nome.split()
print("O primeiro nome é {} e tem {} letras".format(lista[0],len(lista[0])))




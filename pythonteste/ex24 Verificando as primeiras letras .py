cores={'azul':'\033[34m',
       'amarelo':'\033[33m',
       'vermelho':'\033[31m',
       'verde':'\033[32m',
       'roxo':'\033[35m',
       'azulbebe':'\033[36m',
       'cinza':'\033[37m',
       'limpa':'\033[m'}

cidade = str(input("Digite o nome da Cidade: ")).lower().strip()
lista = cidade.split()
palavra = ['santo']

if lista[0] == palavra[0]:
    print("A cidade {} começa com SANTO.".format(cidade).title())
else:
    print("A cidade {} não começa com SANTO.".format(cidade))

cid = str(input("Em que cidade você nasceu? ")).lower().strip()
print(cid[0:5] == 'santo')

    

def valorLista():
    for i in range(1,5):
        lista.append(float(input(f'Digite o valor da sua prova {i}: ')))

def media ():
    s = 0
    for i in range(len(lista)):
        s = s + lista[i]

    m = s / 4
    if m > 7:
        print('O aluno foi Aprovado')
    else:
        print('O aluno foi Reprovado')
    return m

lista = []
valorLista()
m = media()
print('O valor da minha média é',m)

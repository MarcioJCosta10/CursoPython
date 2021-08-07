nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média entre {:1} e {:1} é {:1}'.format(nota1, nota2, media))
if 5 < media:
    print("O aluno foi aprovado! Parabéns!")
else:
    print("O aluno foi reprovado! Você precisa de mais dedicação!")

frase = str(input("Digite uma frase qualquer: ")).upper().strip()
print("Nessa frase a letra A aparece", frase.count('A'))
print("A primera letra A apareceu na posição {} ".format(frase.find('A')+1))# o + um é porque sempre inicia em 0
print("A ultima posição da letra é {} ".format(frase.rfind('A')+1))



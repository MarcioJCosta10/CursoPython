num = str(input("Digite um numero: "))
lista = num
print("Analisando o numero {} ".format(num))
print("Unidade : ",'\033[31m', lista[3] ,'\033[m')
print("Dezena : ",'\033[7;32;44m',lista[2],'\033[m')
print("Centena: ",'\033[4;36;41m',lista[1],'\033[m')
print("Milhar:  ",'\033[1;37;46m',lista[0],'\033[m')

num2 = int(input("Digito outro numero: "))
u = num2 //1 % 10
d = num2 //10 % 10
c = num2 // 100 % 10
m = num2 // 1000 % 10

print("Analisando outro numero {} ".format(num))
print("Unidade : {}".format(u))
print("Dezena :  {}".format(d))
print("Centena : {}".format(c))
print("Milhar :  {}".format(m))


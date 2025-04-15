#Usando While para Somar e tirar a média de 10 Valores!
X=0
Soma=0
while X <10:
    Valor = int(input("Digite um Valor: "))
    Soma += Valor
    X+=1
Media=Soma/10
print(Media)
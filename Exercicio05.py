#Ler dois Valores, Dividir o Primeiro pelo Segundo. Caso o Segundo Valor seja < 0, Solicitar Novamente!
Valor1 = int(input("Digite o Primeiro Valor: "))
Valor2 = int(input("Digite o Segundo Valor: "))
Divisao=0
while Valor2 == 0:
    Valor2 = int(print("Digite o Segundo Valor:"))
Divisao = Valor1 / Valor2
print(Divisao)  
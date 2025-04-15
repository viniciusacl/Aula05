#Escrever um Cod para ler as notas da 1a e 2a. Av de um Aluno, calcular e imprimir a média. Aceitar valores de (0 a 10).
Nota1 = float(input("Digite a Nota da 1a. Av: "))
while Nota1 <0 or Nota1>10:
    Nota1 = float(input("Digite a Nota da 1a. Av: "))
Nota2 = float(input("Digite a Nota da 2a. Av: "))
while Nota2 <0 or Nota1>10:
    Nota2 = float(input("Digite a Nota da 2a. Av: "))
Media=(Nota1+Nota2/2)
print(Media)




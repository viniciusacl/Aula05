#Receber um numero de alunos de uma sala e depois Solicitar as notas desses alunos, no final, Mostrar a media
X=0
Soma=0
Alunos = int(input("Digite o número de Alunos: "))
while X <= Alunos:
    Notas = int(input("Digite Suas Notas: "))
    X+=1
    Soma+=Notas
Media=Soma/2
print(Media)

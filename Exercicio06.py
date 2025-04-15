#Cod para ler a Senha do Usuário e após 3 tentativas, sair do Programa, Informado bloqueio de senha!
Padrao=777
Cont=1
Senha = int(input("Digite sua Senha: "))
while Senha != Padrao and Cont < 3:
    Senha = int(input("Digite sua Senha: "))
    Cont += 1
if Senha == Padrao:
    print("Senha Correta! ")
else:
    print("Senha INCORRETA!!!") 
cadastro_concluido = False
tentativas = 0

print("####################")
print("-- Cadastro de senha --")
print("####################")

while cadastro_concluido != True:
    usuario = input("Digite seu nome: ")
    senha = int(input("Digite a senha desejada: "))
    confirmacao = int(input("Confirme a senha: "))
    if confirmacao == senha:
        print("Cadastro realizado com sucesso!")
        cadastro_concluido = True
    else:
        print("As senhas não coincidem, tente novamente!")

tela_de_bloqueio = input("Deseja desbloquear o smartphone?\n"
                         "[1] - sim\n"
                         "[2] - não\n"
                         "")

if tela_de_bloqueio == "1" or tela_de_bloqueio == "sim":
    desbloqueio = False
    while desbloqueio != True:
        senha_desbloqueio = int(input("Digite sua senha: "))
        if senha_desbloqueio == senha:
            print(f"Acesso concedido. Seja bem-vindo {usuario}")
            desbloqueio = True
        else:
            tentativas += 1
            print(f"Senha incorreta. Tentativa {tentativas} de 3!")
        if tentativas >= 3:
            print("Número maximo de tentativas excedido. O aparelho será bloqueado!")
            print("Contate a central do aparelho para Reset do mesmo!")
            break
else:
    print("Aparelho corrompido, reiniciando de fabrica!")

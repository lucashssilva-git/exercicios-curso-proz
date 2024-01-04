print("Digite seu nome completo: ")
nome = input()

usuario = True

while (usuario == True):
    print("Digite o seu ano de nascimento: ")

    try:
        ano = int(input())
        if (ano < 1922) or (ano > 2024):
            print("O ano precisa ser entre 1922 à 2024")
        else:
            idade = 2024 - ano
            print("O usuário(a)", nome, "fez ou fará", idade, "Anos em 2024")
            
            usuario = False
            

    except:("ERRO: Digite os anos apenas em números.")
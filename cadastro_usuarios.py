usuarios = {}

while True:
    print("\n=== SISTEMA DE CADASTRO ===")
    print("1 - Cadastrar usuário")
    print("2 - Ver usuários")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")

        usuarios[nome] = idade
        print("Usuário cadastrado com sucesso! ✅")

    elif opcao == "2":
        print("\nLista de usuários:")

        for nome, idade in usuarios.items():
            print(f"Nome: {nome} | Idade: {idade}")

    elif opcao == "3":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")
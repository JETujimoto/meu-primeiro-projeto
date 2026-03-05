alunos = set()

while True:
    print("\n=== SISTEMA DE ALUNOS ===")
    print("1 - Adicionar aluno")
    print("2 - Ver alunos")
    print("3 - Sair")

    opcao = input("Escolha uma opção:")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")

        if nome in alunos:
            print("Aluno já cadastrado!")
        else:
            alunos.add(nome)
            print("Aluno adicionado com sucesso! ✅")

    elif opcao == "2":
        print("\nLista de alunos:")
        for aluno in alunos:
            print(aluno)

    elif opcao == "3":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")
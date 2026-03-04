lista = []

while True:
    print("\n=== LISTA DE COMPRAS ===")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o nome do item: ")
        lista.append(item)
        print("Item adicionado com sucesso! ✅")

    elif opcao == "2":
        item = input("Digite o item que deseja remover: ")
        if item in lista:
            lista.remove(item)
            print("Item removido! ❌")
        else:
            print("Item não encontrado!")

    elif opcao == "3":
        print("\nItens na lista:")
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")

    elif opcao == "4":
        print("Saindo... 👋")
        break

    else:
        print("Opção inválida!")
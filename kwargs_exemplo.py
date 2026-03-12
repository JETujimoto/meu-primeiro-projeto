def mostrar_dados(**kwargs):

    print("Dados recebidos:")

    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")


mostrar_dados(nome="José", idade=25, cidade="Rio Preto")
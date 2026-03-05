print("=== LOJA VIRTUAL ===")

# Tupla de produtos (nome, preço)
produtos = (
    ("Arroz", 20.50),
    ("Feijão", 8.30),
    ("Macarrão", 5.90),
    ("Óleo", 7.40),
)

# Mostrar produtos
print("\nLista de produtos:")
for nome, preco in produtos:
    print(f"{nome} - R$ {preco}")

# Calcular valor total
total = 0
for _, preco in produtos:
    total += preco

print(f"\nValor total de todos os produtos: R$ {total}")

# Buscar produto
busca = input("\nDigite o nome do produto para buscar: ")

encontrado = False
for nome, preco in produtos:
    if nome.lower() == busca.lower():
        print(f"Produto encontrado: {nome} custa R$ {preco}")
        encontrado = True

if not encontrado:
    print("Produto não encontrado.")
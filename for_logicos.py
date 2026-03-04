print("=== Verificador de Números ===")

for i in range(5):
    numero = int(input(f"\nDigite o número {i+1}: "))

    if numero > 0 and numero % 2 == 0:
        print("Número positivo e par ✅")

    elif numero < 0 or numero == 0:
        print("Número negativo ou zero ⚠")

    elif not numero > 0:
        print("Número não é positivo")

    else:
        print("Número positivo e ímpar 🔵")
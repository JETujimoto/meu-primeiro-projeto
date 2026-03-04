print("=== CALCULADORA ===")

for i in range(5):
    print(f"\nCálculo {i + 1}")

    num1 = float(input("Digite o primeiro número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: divisão por zero!")
            continue
    else:
        print("Operador inválido!")
        continue

    print("Resultado:", resultado)
import random

numero_secreto = random.randint(1, 10)

print("=== JOGO DE ADIVINHAÇÃO ===")
print("Tente adivinhar o número de 1 a 10")

while True:
    tentativa = int(input("Digite seu palpite: "))

    if tentativa == numero_secreto:
        print("Parabéns! Você acertou 🎉")
        break
    elif tentativa < numero_secreto:
        print("O número é maior 🔼")
    else:
        print("O número é menor 🔽")
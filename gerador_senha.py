import random

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"

tamanho = int(input("Digite o tamanho da senha: "))

senha = ""

for i in range(tamanho):
    senha += random.choice(caracteres)

print("Senha gerada:", senha)
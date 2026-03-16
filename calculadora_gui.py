import tkinter as tk

# função de soma
def somar():
    n1 = float(entrada1.get())
    n2 = float(entrada2.get())
    resultado = n1 + n2
    label_resultado.config(text=f"Resultado: {resultado}")

# criar janela
janela = tk.Tk()
janela.title("Calculadora Simples")

# campos de entrada
entrada1 = tk.Entry(janela)
entrada1.pack()

entrada2 = tk.Entry(janela)
entrada2.pack()

# botão
botao = tk.Button(janela, text="Somar", command=somar)
botao.pack()

# resultado
label_resultado = tk.Label(janela, text="Resultado:")
label_resultado.pack()

# iniciar interface
janela.mainloop()
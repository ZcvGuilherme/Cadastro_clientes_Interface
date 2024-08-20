import tkinter as tk
from tkinter import font

def list_fonts():
    root = tk.Tk()
    root.title("Fonts in Tkinter")

    # Obter todas as fontes disponíveis
    fonts = font.families()

    # Criar um canvas para listar as fontes
    canvas = tk.Canvas(root, width=600, height=400)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.configure(yscrollcommand=scrollbar.set)
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Adicionar todas as fontes à tela
    for i, f in enumerate(fonts):
        tk.Label(frame, text=f, font=(f, 12)).pack(anchor="w", pady=2, padx=10)

    # Atualizar o tamanho da área de rolagem
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    root.mainloop()

list_fonts()

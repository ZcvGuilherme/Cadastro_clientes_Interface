import tkinter as tk

def on_button_click(event, message):
    print(message)
    print(f"Evento gerado por: {event.widget}")

root = tk.Tk()

# Cria um botão
button = tk.Button(root, text="Clique Aqui")
button.pack(padx=20, pady=20)

# Usa uma função lambda para passar o argumento 'Olá, Mundo!' para o manipulador
button.bind("<Button-1>", lambda event: on_button_click(event, "Olá, Mundo!"))

root.mainloop()

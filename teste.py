import tkinter as tk
from autocompletar import AutoCompleteEntry

root = tk.Tk()
root.title("Main Interface")
root.geometry("300x150")

entry = AutoCompleteEntry(
    master=root,
    lista=[
        "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal", "Espírito Santo",
        "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba",
        "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul",
        "Rondônia", "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
    ],
    max_suggestions=5
)
entry.pack(pady=20, padx=10)

root.mainloop()

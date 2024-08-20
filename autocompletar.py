import tkinter as tk

class AutoCompleteEntry(tk.Entry):
    def __init__(self, master=None, lista=None, max_suggestions=5, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.lista = lista if lista else []
        self.var = tk.StringVar()
        self.config(textvariable=self.var)
        self.var.trace("w", self.on_write)
        self.listbox = None
        self.max_suggestions = max_suggestions

    def on_write(self, *args):
        typed_text = self.var.get()
        if typed_text == "":
            self.hide_listbox()
        else:
            matches = [item for item in self.lista if item.lower().startswith(typed_text.lower())]
            if matches:
                if self.listbox is None:
                    self.show_listbox(matches)
                else:
                    self.update_listbox(matches)
            else:
                self.hide_listbox()

    def show_listbox(self, matches):
        if self.listbox is None:
            self.listbox = tk.Listbox(self.master, height=min(len(matches), self.max_suggestions))
            self.listbox.bind("<<ListboxSelect>>", self.on_listbox_select)
            self.listbox.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height(), width=self.winfo_width())

        self.update_listbox(matches)

    def update_listbox(self, matches):
        if self.listbox:
            self.listbox.delete(0, tk.END)
            for match in matches:
                self.listbox.insert(tk.END, match)
                self.listbox.itemconfig(tk.END, {'bg': '#f0f0f0', 'selectbackground': '#d0d0d0'})  # Estilo simples

            self.listbox.config(height=min(len(matches), self.max_suggestions))

    def hide_listbox(self):
        if self.listbox is not None:
            self.listbox.destroy()
            self.listbox = None

    def on_listbox_select(self, event):
        if self.listbox:
            selection = self.listbox.get(self.listbox.curselection())
            self.var.set(selection)
            self.hide_listbox()

root = tk.Tk()
root.title("Autocomplete Entry")
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

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
        self.font = kwargs.get('font', ('Nirmala UI', 7))  # Definir fonte padrão ou usar a fornecida

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
            self.listbox = tk.Listbox(
                self.master,
                font=self.font,  # Definindo a fonte da Listbox
                height=min(len(matches), self.max_suggestions)
            )
            self.listbox.bind("<<ListboxSelect>>", self.on_listbox_select)
            self.listbox.place(
                x=self.winfo_x(), 
                y=self.winfo_y() + self.winfo_height(), 
                width=self.winfo_width()
            )

        self.update_listbox(matches)

    def update_listbox(self, matches):
        if self.listbox:
            self.listbox.delete(0, tk.END)
            for match in matches:
                self.listbox.insert(tk.END, match)
                self.listbox.itemconfig(tk.END, {'bg': '#f0f0f0', 'selectbackground': '#d0d0d0'})

            self.listbox.config(
                height=min(len(matches), self.max_suggestions),
                width=self.calculate_listbox_width(matches)
            )

    def calculate_listbox_width(self, matches):
        # Calcula a largura necessária para a Listbox com base no texto mais longo
        longest_match = max(matches, key=len)
        return max(len(longest_match), self.winfo_width())//2  # Ajuste conforme necessário

    def hide_listbox(self):
        if self.listbox is not None:
            self.listbox.destroy()
            self.listbox = None

    def on_listbox_select(self, event):
        if self.listbox:
            selection = self.listbox.get(self.listbox.curselection())
            self.var.set(selection)
            self.hide_listbox()
    
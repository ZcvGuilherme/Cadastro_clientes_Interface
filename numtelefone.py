import tkinter as tk

class MinhaApp:
    def __init__(self, root):
        self.frame1 = tk.Frame(root)
        self.frame1.pack()

        # Função para validar a entrada
        def validar_digitos(entry_text):
            return entry_text.isdigit() and len(entry_text) <= 3

        # Configuração da função de validação
        validate_cmd = root.register(validar_digitos)

        # Configuração da Entry para aceitar no máximo 3 dígitos numéricos
        self.entry_idade = tk.Entry(
            self.frame1, 
            justify='center', 
            font=('Nirmala UI', 15, 'bold'), 
            bd=2, 
            cursor='xterm', 
            highlightcolor='#9ACD32', 
            highlightthickness=2,
            validate="key", 
            validatecommand=(validate_cmd, '%P')
        )
        self.entry_idade.place(relx=0.5, rely=0.15, relheight=0.09, relwidth=0.13)

if __name__ == "__main__":
    root = tk.Tk()
    app = MinhaApp(root)
    root.mainloop()

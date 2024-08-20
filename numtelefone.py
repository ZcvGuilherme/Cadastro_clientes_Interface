import tkinter as tk

def format_phone_number(entry_text):
    # Remove qualquer caractere que não seja número
    digits = ''.join([char for char in entry_text if char.isdigit()])
    
    # Limite de 11 dígitos (excluindo parênteses e traço)
    if len(digits) > 11:
        digits = digits[:11]

    if len(digits) > 7:
        return f"({digits[:2]}) {digits[2:7]}-{digits[7:]}"
    elif len(digits) > 2:
        return f"({digits[:2]}) {digits[2:7]}"
    elif len(digits) > 0:
        return f"({digits})"
    else:
        return ""

def on_key_release(event):
    entry = event.widget
    formatted_text = format_phone_number(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, formatted_text)

# Configuração básica da janela
root = tk.Tk()
root.title("Entrada de Telefone")
root.geometry("300x100")

# Criação da Entry
phone_entry = tk.Entry(root)
phone_entry.pack(pady=20)
phone_entry.bind('<KeyRelease>', on_key_release)

root.mainloop()

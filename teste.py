import tkinter as tk

root = tk.Tk()
root.configure(bg='#FFFFFF')

frame = tk.Frame(root, bg='#DCDCDC')
frame.pack(padx=20, pady=20)

# Definir as cores para o Checkbutton
check_var = tk.IntVar()
checkbutton = tk.Checkbutton(frame, text="Opção 1", variable=check_var,
                             bg='#DCDCDC',  # Cor de fundo igual ao Frame
                             activebackground='#DCDCDC',  # Cor de fundo quando ativo
                             selectcolor='lightgreen',  # Cor do fundo da caixa quando marcada
                             relief='flat')  # Sem borda para não destoar
checkbutton.pack()

root.mainloop()

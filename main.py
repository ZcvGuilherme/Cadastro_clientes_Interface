import tkinter as tk
from tkinter import *

#criar uma tela
root = tk.Tk()
class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.Frames_Tela()
        self.Entradas()
        root.mainloop()
    def tela(self):
        self.root.title('CADASTRO CLIENTES')
        self.root.configure(background='#DCDCDC')
        self.root.geometry('800x700')
        self.root.resizable(False, False)
        self.root.minsize(width=300, height=300)
        icone = tk.PhotoImage(file='avatar.png')
        self.root.iconphoto(True, icone)
    def Frames_Tela(self):
        self.frame1 = Frame(self.root, bd=4, bg='#c0dcc0',relief='ridge')
        self.frame1.place(relx=0.05, rely=0.02, relheight=0.65, relwidth=0.9)

        self.frame2 = Frame(self.root, bd=4, bg='white', relief='groove')
        self.frame2.place(relx=0.05, rely=0.70, relheight=0.25, relwidth=0.9)
    def Entradas(self):
        #------------------------ENTRY NOME-------------------------------------------------#
        self.entry_nome = Entry(self.frame1, justify='left', font=('Arial',11, 'bold'),bd= 4, cursor='xterm')
        self.entry_nome.place(relx=0.03, rely=0.12, relheight=0.09, relwidth=0.3)
        self.label_nome = Label(self.frame1, justify='center', font=('Verdana', 15, 'bold italic'), text='Nome', bg='#f0f0f0',border=2, relief='groove', padx=1, pady=1)
        self.label_nome.place(relx=0.03, rely=0.01, relheight=0.07, relwidth=0.3)
        #----------------------------------------------------------------------------------#

tela = Application()

import tkinter as tk
from tkinter import *

#criar uma tela
root = tk.Tk()
class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.Frames_Tela()
        self.botoes()
        root.mainloop()
    def tela(self):
        self.root.title('CADASTRO CLIENTES')
        self.root.configure(background='#DCDCDC')
        self.root.geometry('600x700')
        self.root.resizable(False, False)
        self.root.minsize(width=300, height=300)
        icone = tk.PhotoImage(file='avatar.png')
        self.root.iconphoto(True, icone)
    def Frames_Tela(self):
        self.frame1 = Frame(self.root, bd=4, bg='#c0dcc0',relief='ridge')
        self.frame1.place(relx=0.05, rely=0.02, relheight=0.65, relwidth=0.9)

        self.frame2 = Frame(self.root, bd=4, bg='white', relief='groove')
        self.frame2.place(relx=0.05, rely=0.70, relheight=0.25, relwidth=0.9)
    def botoes(self):
        self.lb_player1 = Label(self.root, relief=RIDGE, text='PLAYER 1', font=('Segoe UI Symbol', 25, 'bold'), bg= '#FF6347')
        self.lb_player1.place(relx=0.15, rely=0.001, relheight=0.1, relwidth=0.2)

        self.cadastrar_Entry = Entry(self.frame1,justify=CENTER, font=('Roman', 50, 'bold'), bd= 4)
        self.cadastrar_Entry.place(relx=0.01, rely=0.01, relheight=0.2, relwidth=0.99)
        self.cadastrar_Entry.insert(0, 8000) 

tela = Application()

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
    def Entradas(self):
        #----------------------------------ENTRY NOME-------------------------------------------------#
        self.entry_nome = Entry(self.frame1, justify='left', font=('Arial',11, 'bold'),bd= 2, cursor='xterm', highlightcolor='#9ACD32', highlightthickness=2, fg='gray')
        self.entry_nome.place(relx=0.03, rely=0.1, relheight=0.09, relwidth=0.3)
        self.set_placeholder(self.entry_nome, 'Digite o nome aqui...')

        self.label_nome = Label(self.frame1, justify='center', font=('Verdana', 15, 'bold italic'), text='Nome', bg='#f0f0f0',border=2, relief='groove', padx=1, pady=1)
        self.label_nome.place(relx=0.03, rely=0.01, relheight=0.07, relwidth=0.3)
        #----------------------------------ENTRY IDADE------------------------------------------------#
        self.entry_idade = Entry(self.frame1, justify='center', font=('Arial',15, 'bold'),bd= 2, cursor='xterm', highlightcolor='#9ACD32', highlightthickness=2)

        self.entry_idade.place(relx=0.4, rely=0.1, relheight=0.09, relwidth=0.13)
        self.label_idade = Label(self.frame1, justify='center', font=('Verdana', 15, 'bold italic'), text='Idade', bg='#f0f0f0',border=2, relief='groove', padx=1, pady=1)
        self.label_idade.place(relx=0.38, rely=0.01, relheight=0.08, relwidth=0.17)
        #----------------------------------ENTRY EMAIL------------------------------------------------#
        self.entry_email = Entry(self.frame1, justify='left', font=('Arial',11, 'bold'),bd= 2, cursor='xterm', highlightcolor='#9ACD32', highlightthickness=2, fg='gray')
        self.entry_email.place(relx=0.03, rely=0.34, relheight=0.09, relwidth=0.5)
        self.set_placeholder(self.entry_email, 'EX:. guilhermesousa@gmail.com')

        self.label_email = Label(self.frame1, justify='center', font=('Verdana', 15, 'bold italic'), text='Email', bg='#f0f0f0',border=2, relief='groove', padx=1, pady=1)
        self.label_email.place(relx=0.13, rely=0.26, relheight=0.07, relwidth=0.3)
        #----------------------------------ENTRY GENERO-----------------------------------------------#
        self.label_genero = Label(self.frame1, justify='center', font=('Verdana', 15, 'bold italic'), text='Gênero', bg='#f0f0f0', border=2, relief='groove')
        self.label_genero.place(relx=0.7, rely=0.01, relheight=0.08, relwidth=0.17)
        #opção masculino
        self.masculino_var = IntVar()
        self.masculino_check = Checkbutton(self.frame1, text="Masculino",font=('Calibri', 16), variable=self.masculino_var, justify='left', bg='#c0dcc0',command=self.select_masculino, relief= 'flat', activebackground='#c0dcc0')
        self.masculino_check.place(relx=0.7, rely=0.1, relheight=0.07, relwidth=0.3)
        #opção feminino
        self.feminino_var = IntVar()
        self.feminino_check = tk.Checkbutton(self.frame1, text="Feminino",font= ('Calibri', 16),variable=self.feminino_var,justify='left',bg='#c0dcc0',activebackground= '#c0dcc0',command=self.select_feminino, selectcolor='white', relief='flat')
        self.feminino_check.place(relx=0.7, rely=0.22, relheight=0.07, relwidth=0.3)
        #----------------------------------ENTRY CIDADE-----------------------------------------------#
        #----------------------------------ENTRY CELULAR----------------------------------------------#

    def botoes(self):
        self.salvar_Button = Button(self.frame1, text="Enviar", command=self.submit)
        self.salvar_Button.place(relx=0.8, rely=0.9, relheight=0.08, relwidth=0.1)

    def set_placeholder(self, entry, placeholder):
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda event: self.on_focus_in(event, placeholder))
        entry.bind("<FocusOut>", lambda event: self.on_focus_out(event, placeholder))

    def on_focus_in(self, event, placeholder_text):
        entry = event.widget
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def on_focus_out(self, event, placeholder_text):
        entry = event.widget
        if entry.get() == "":
            entry.insert(0, placeholder_text)
            entry.config(fg='gray')

    def select_masculino(self):
        if self.masculino_var.get() == 1:
            self.feminino_var.set(0)

    def select_feminino(self):
        if self.feminino_var.get() == 1:
            self.masculino_var.set(0)
tela = Application()

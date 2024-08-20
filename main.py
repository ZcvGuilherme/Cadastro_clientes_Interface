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
        self.frame1.place(relx=0.05, rely=0.02, relheight=0.5, relwidth=0.9)

        self.frame2 = Frame(self.root, bd=4, bg='white', relief='groove')
        self.frame2.place(relx=0.05, rely=0.55, relheight=0.4, relwidth=0.9)
    def Entradas(self):
        #----------------------------------ENTRY NOME-------------------------------------------------#
        self.entry_nome = Entry(self.frame1, justify='left', font=('Nirmala UI ',11, 'bold'),bd= 2, cursor='xterm', highlightcolor='#9ACD32', highlightthickness=2, fg='gray')
        self.entry_nome.place(relx=0.03, rely=0.15, relheight=0.09, relwidth=0.4)
        self.set_placeholder(self.entry_nome, 'Digite o nome aqui...')

        self.label_nome = Label(self.frame1, justify='center', font=('Nirmala UI', 15, 'bold'), text='Nome', bg='#f0f0f0',border=2, relief='groove', padx=1, pady=1)
        self.label_nome.place(relx=0.08 , rely=0.02, relheight=0.09, relwidth=0.3)
        #----------------------------------ENTRY IDADE------------------------------------------------#
        self.entry_idade = Entry(self.frame1, justify='center', font=('Nirmala UI',15, 'bold'),bd= 2, cursor='xterm', highlightcolor='#9ACD32', highlightthickness=2)
        self.entry_idade.place(relx=0.5, rely=0.15, relheight=0.09, relwidth=0.13)

        self.label_idade = Label(self.frame1, justify='center', font=('Nirmala UI', 15, 'bold'), text='Idade', bg='#f0f0f0',border=2, relief='groove', padx=1, pady=1)
        self.label_idade.place(relx=0.48, rely=0.02, relheight=0.09, relwidth=0.17)
        #----------------------------------ENTRY EMAIL------------------------------------------------#
        self.entry_email = Entry(self.frame1, justify='left', font=('Nirmala UI', 15, 'bold'),bd= 2, cursor='xterm', highlightcolor='#9ACD32', highlightthickness=2, fg='gray')
        self.entry_email.place(relx=0.01, rely=0.38, relheight=0.09, relwidth=0.5)
        self.set_placeholder(self.entry_email, 'EX:. guilhermesousa@gmail.com')

        self.label_email = Label(self.frame1, justify='center', font=('Verdana', 15, 'bold italic'), text='Email', bg='#f0f0f0',border=2, relief='groove', padx=1, pady=1)
        self.label_email.place(relx=0.08, rely=0.26, relheight=0.09, relwidth=0.3)
        #----------------------------------ENTRY GENERO-----------------------------------------------#
        self.label_genero = Label(self.frame1, justify='center', font=('Verdana', 15, 'bold italic'), text='Gênero', bg='#f0f0f0', border=2, relief='groove')
        self.label_genero.place(relx=0.7, rely=0.01, relheight=0.08, relwidth=0.17)
        #opção masculino
        self.masculino_var = IntVar()
        self.masculino_check = Checkbutton(self.frame1, text="Masculino",font=('Calibri', 16), variable=self.masculino_var, justify='left', bg='#c0dcc0',command=self.select_masculino, relief= 'flat', activebackground='#c0dcc0')
        self.masculino_check.place(relx=0.65, rely=0.1, relheight=0.07, relwidth=0.3)
        #opção feminino
        self.feminino_var = IntVar()
        self.feminino_check = tk.Checkbutton(self.frame1, text="Feminino",font= ('Calibri', 16),variable=self.feminino_var,justify='left',bg='#c0dcc0',activebackground= '#c0dcc0',command=self.select_feminino, selectcolor='white', relief='flat')
        self.feminino_check.place(relx=0.643, rely=0.22, relheight=0.07, relwidth=0.3)
        #----------------------------------ENTRY CIDADE-----------------------------------------------#
        self.label_cidade = Label(self.frame1, justify='center', font=('Verdana', 15, 'bold italic'), text='Cidade', bg='#f0f0f0', border=2, relief='groove')
        self.label_cidade.place(relx=0.8, rely=0.35, relheight=0.08, relwidth=0.17)

        self.entry_cidade = Entry(self.frame1, justify='left', font=('Nirmala UI', 15, 'bold'),bd= 2, cursor='xterm', highlightcolor='#9ACD32', highlightthickness=2, fg='gray')
        self.entry_cidade.place(relx=0.8, rely=0.45, relheight=0.09, relwidth=0.17)

        #----------------------------------ENTRY ESTADO-----------------------------------------------#
        self.label_estado = Label(self.frame1, justify='center', font=('Verdana', 15, 'bold italic'), text='Estado', bg='#f0f0f0', border=2, relief='groove')
        self.label_estado.place(relx=0.6, rely=0.35, relheight=0.08, relwidth=0.17)

        self.entry_cidade = Entry(self.frame1, justify='left', font=('Nirmala UI', 15, 'bold'),bd= 2, cursor='xterm', highlightcolor='#9ACD32', highlightthickness=2)
        self.entry_cidade.place(relx=0.6, rely=0.45, relheight=0.09, relwidth=0.17)
        #----------------------------------ENTRY CELULAR----------------------------------------------#
        self.entry_celular = Entry(self.frame1, justify='left', font=('Arial',15, 'bold'),bd= 2, cursor='xterm', highlightcolor='#9ACD32', highlightthickness=2, fg='black')
        self.entry_celular.place(relx=0.08, rely=0.6, relheight=0.1, relwidth=0.3)

        self.label_celular = Label(self.frame1, justify='center', font=('Verdana', 15, 'bold italic'), text='Celular', bg='#f0f0f0', border=2, relief='groove')
        self.label_celular.place(relx=0.08, rely=0.5, relheight=0.09, relwidth=0.3)
        #----------------------------------------------------------------------------------------------#
    def botoes(self):
        self.salvar_img = PhotoImage(file="disquete(1).png")
        self.salvar_Button = Button(self.frame1, image=self.salvar_img, relief='flat', bd=4, bg='#c0dcc0')
        self.salvar_Button.place(relx=0.85, rely=0.75, relheight=0.13, relwidth=0.1)

        self.apagar_img = PhotoImage(file='fechar.png')
        self.apagar_Button = Button(self.frame1, image=self.apagar_img, relief='flat', bd=4, bg='#c0dcc0')
        self.apagar_Button.place(relx=0.65, rely=0.75, relheight=0.13, relwidth=0.1)
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

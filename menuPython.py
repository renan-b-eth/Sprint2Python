from tkinter import *
from tkinter import ttk
import tkinter as tk

from PIL import ImageTk, Image

import os

root = Tk()
root.geometry("500x500")
root.title("Menu Basico de Python")
root.resizable(False, False)


#criacao menu

menu = Menu(root)
root.config(Menu=menu)

File = Menu(menu)
Edit = Menu(menu)
Help = Menu(menu)

menu.add_cascade(label= "File" , menu= File)

def semComando():
    print("")

    #menu aqui
barraMenu = Menu(root)
#menuOpcao1 = Menu(barraMenu)
#menuOpcao1.add_command(label="Opcao1", command=semComando)
#menuOpcao1.add_command(label="Opcao2", command=semComando)
#menuOpcao1.add_command(label="Opcao3", command=semComando)
#menuOpcao1.add_separator()
#menuOpcao1.add_command(label="Sair", command=root.quit)
#root.config(menu=barraMenu)

#img = PhotoImage(file="C:/Users/logonrmlocal/Desktop/pasta/menuPython/imagens/logo8.png")
#lbl_img = Label(root, image=img).pack()



def abrirSegundaTela():
    root2 = Tk()
    root2.geometry("1000x1000")
    root2.title("Menu Basico de Python")
    frame2 = ttk.Frame(root2, padding=100)
    #label2 = ttk.Label(frame, text="outro", background="blue", font="50", padding="10").grid(column=1, row=0)
    
#criacao do menu v2

#main_frame = tk.Frame(root, height=False)
#main_frame.pack(fill=tk.BOTH, expand=True)
#main_frame.columnconfigure(0, weight=1)
#main_frame.rowconfigure(0, weight=0)

#cbg1 = '#cbbaff'
#cfg1 = 'BLACK'

#v = tk.StringVar()
#v.set("Escolha uma opção")

#lista_opcoes = ['Primeira', 'Segunda', 'Terceira']

#lista_opcoes = tk.OptionMenu(
    #main_frame,
    #v,
    #*lista_opcoes
#)

frame = ttk.Frame(root, padding=100)
label = ttk.Label(frame, text="Menu InovaAcess", background="blue", font="50").grid(column=0, row=0)

ttk.Button(frame, text="Quit", command=root.destroy).grid(column=4, row=1)
ttk.Button(frame, text="Nova Operação", command = abrirSegundaTela).grid(column=2, row=1)


frame.grid()
root.mainloop()



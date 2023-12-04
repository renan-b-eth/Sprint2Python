from tkinter import *
from tkinter import messagebox
import tkinter as tk
import webbrowser
import subprocess
import os

root = Tk()
#criacao menu
menu= Menu(root)
root.config(menu=menu)
root.title("Menu InovaAcess - Segunda Sprint")
root.geometry("500x500")
#fundo = PhotoImage(file="logo8.png")
#fundo1 = Label(root, image=fundo).place(x=1, y=1, relheight=1, relwidth=1)
root.resizable(False, False)


def acessarSiteProdutos(url):
    return webbrowser.open(url)


def sfuncionalidade():

    root2 = Tk()
    root2.geometry("800x500")
    root2.title("2 - Funcionalidade")

    messagebox.showinfo("Texto 2 - Funcionaldiade"," As pessoas surdas ou com deficiência auditiva que se comunicam através da Língua de Sinais, são conhecidas como “sinalizantes”. Muitas delas possuem grande dificuldade com as línguas escritas e, por isso, a comunicação em Libras proporciona liberdade e autonomia no seu dia a dia. Com acessibilidade em Libras elas conseguem receber na sua língua materna todas as informações que estão sendo transmitidas em Português. Isso é fundamental para garantir sua inclusão na sociedade, nas escolas e universidades, no mercado de trabalho, na sua lista de clientes, etc. Com base nessa informação, iremos implantar um sistema de hand talk, onde a pessoa irá selecionar a opção desejada pelo assistente virtual, e logo será direcionada.")


def tfuncionalidade():
    root2 = Tk()
    root2.geometry("500x500")
    root2.title("3 - Funcionalidade - Futuramente")

def qfuncionalidade():
    root2 = Tk()
    root2.geometry("500x500")
    root2.title("4 - Funcionalidade - Futuramente")

def quemSomos():
    messagebox.showinfo("Quem Somos?", "Larissa Kawaguti Feliciano - 553356\nLucas Alcântara Carvalho - 95111\nRenan Bezerra dos Santos - 553228")

def acessarDiretorio(diretorio):
   return os.startfile(diretorio)

def acessarCameraMouse():
    return None
   

def sregra():
    messagebox.showinfo("2 - Regra de Negócio", "Usabilidade Intuitiva: Garantir que o sistema seja fácil de usar, com instruções claras para ativar e desativar a funcionalidade do mouse baseado em câmera, para permitir a acessibilidade para pessoas com dificuldades motoras.")

opcao1 = Menu(menu, tearoff=0)
opcao1.add_command(label= "Acessar Site Produtos", command= lambda: acessarSiteProdutos("https://www.salesforce.com/br/products/"))

opcao2 = Menu(menu, tearoff=0)
opcao2.add_command(label= "Acessar Camera Mouse", command= lambda: acessarCameraMouse)
opcao2.add_command(label= "Acessar Teclado Virtual", command=lambda: acessarDiretorio('C:\\Windows\\System32\\osk.exe'))

sobrenos = Menu(menu, tearoff=0)
sobrenos.add_command(label= "Quem somos", command=quemSomos)

sair = Menu(menu, tearoff=0)
sair.add_command(label="Sair", command=exit)


menu.add_cascade(label = "Produtos", menu= opcao1)
menu.add_cascade(label = "Acessibilidade", menu= opcao2)
menu.add_cascade(label = "Quem somos", menu= sobrenos)
menu.add_cascade(label = "Sair", menu= sair)


root.mainloop()
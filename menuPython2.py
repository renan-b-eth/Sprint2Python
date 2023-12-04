from tkinter import *
from tkinter import messagebox
import tkinter as tk
import webbrowser
import subprocess
import os
import pyautogui
import time
import random
 
root = Tk()
#criacao menu
menu= Menu(root)
root.config(menu=menu)
root.title("Menu InovaAcess - Segunda Sprint")
root.geometry("900x500")
#fundo = PhotoImage(file="logo8.png")
#fundo1 = Label(root, image=fundo).place(x=1, y=1, relheight=1, relwidth=1)
root.resizable(False, False)
 
 
def criarBotao():
    #deixar dinamico na sprint3 (aqui é feito o prototipo basico pois iremos usar o tasorflow js
    # ao inves do opencv,
    # o python no backend será utilizado para outros fins e para aproveitar suas bibliotecas.)
    btnMoverMouse = Button(root, text = 'Mover Camera',
                       command = lambda: moverCameraMouse(50,50,2))                  
    btnMoverMouse.place(x=450, y=300, anchor=CENTER)
    btnMoverMouse.configure(height=5, width=15, bg="#CADFEE")
   
 
def acessarSiteProdutos(url):
    return webbrowser.open(url)
 
 
def quemSomos():
    messagebox.showinfo("Quem Somos?", "Larissa Kawaguti Feliciano - 553356\nLucas Alcântara Carvalho - 95111\nRenan Bezerra dos Santos - 553228")
 
def acessarDiretorio(diretorio):
   return os.startfile(diretorio)
 
#mover o mouse
def moverCameraMouse(x,y, segundos):
    i = 1
    while True:
        i = i + 1
        for y in range(5):
            time.sleep(0.5)
            pyautogui.moveTo(x,y,duration=segundos)
        if(i > 3):
            break
     
     
 
   
 
def sregra():
    messagebox.showinfo("2 - Regra de Negócio", "Usabilidade Intuitiva: Garantir que o sistema seja fácil de usar, com instruções claras para ativar e desativar a funcionalidade do mouse baseado em câmera, para permitir a acessibilidade para pessoas com dificuldades motoras.")
 
opcao1 = Menu(menu, tearoff=0)
opcao1.add_command(label= "Acessar Produtos", command= lambda: acessarSiteProdutos("https://www.salesforce.com/br/products/"))
 
opcao2 = Menu(menu, tearoff=0)
opcao2.add_command(label= "Acessar Camera Mouse", command= lambda: criarBotao())

opcao3 = Menu(menu, tearoff=0)
opcao3.add_command(label= "Acessar Teclado Virtual", command=lambda: acessarDiretorio('C:\\Windows\\System32\\osk.exe'))
 
sobrenos = Menu(menu, tearoff=0)
sobrenos.add_command(label= "Quem somos", command=quemSomos)
 
sair = Menu(menu, tearoff=0)
sair.add_command(label="Sair", command=exit)
 
 
menu.add_cascade(label = "Produtos      ", menu= opcao1)
menu.add_cascade(label = "Acessibilidade - Camera Mouse      ", menu= opcao2)
menu.add_cascade(label = "Acessibilidade - Teclado Virtual      ", menu= opcao3)
menu.add_cascade(label = "Quem somos      ", menu= sobrenos)
menu.add_cascade(label = "Sair", menu= sair)
 
 
root.mainloop()
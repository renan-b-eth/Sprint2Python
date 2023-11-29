from tkinter import *
from tkinter import messagebox
import tkinter as tk

root = Tk()
#criacao menu
menu= Menu(root)
root.config(menu=menu)
root.title("Menu InovaAcess - Primeira Sprint")
root.geometry("500x500")
fundo = PhotoImage(file="logo8.png")
fundo1 = Label(root, image=fundo).place(x=1, y=1, relheight=1, relwidth=1)
root.resizable(False, False)


#var = tk.StringVar()
#var.set("TITULO PRIMEIRA FUNCIONALIDADE")
#mylabel = tk.Label(root, textvariable=var)
#mylabel.pack()




def pfuncionalidade():
    root2 = Tk()
    root2.geometry("500x500")
    root2.title("1 - Funcionalidade")

    var = tk.StringVar()
    #var.set("abriu")
    mylabel = tk.Label(root, textvariable=var)
    mylabel.pack()

    messagebox.showinfo('Texto 1 - Funcionalidade ', \
      'Pensando nisso, optamos a princípio em implantar um sistema onde a pessoa quase não irá precisar fazer o uso do mouse. Ela apenas terá que determinar um ponto de foco no seu rosto, para que faça a função do mouse. E movimentando o rosto, irá movimentar o mouse automaticamente, sem precisar fazer o uso das mãos. Para ativar esse recurso, a pessoa terá que selecionar a opção desejada no assistente virtual, permitir o acesso a imagem, ativando assim, o recurso de câmera mouse.')
    
    #esse codigo não funciona 
    #var = tk.StringVar()
    #var.set("TITULO PRIMEIRA FUNCIONALIDADE")
    #mylabel = tk.Label(root2, textvariable=var)
    #mylabel.pack()


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

def pregra():
    messagebox.showinfo("1 - Regra de Negócio", "Privacidade e Consentimento: Garantir que os usuários entendam e concordem com o uso da câmera para a funcionalidade do mouse e que os dados capturados sejam protegidos de acordo com as regulamentações de privacidade.")

def sregra():
    messagebox.showinfo("2 - Regra de Negócio", "Usabilidade Intuitiva: Garantir que o sistema seja fácil de usar, com instruções claras para ativar e desativar a funcionalidade do mouse baseado em câmera, para permitir a acessibilidade para pessoas com dificuldades motoras.")

opcao1 = Menu(menu, tearoff=0)
opcao1.add_command(label= "1 - Funcionalidade", command=pfuncionalidade)
opcao1.add_command(label= "2 - Funcionalidade", command=sfuncionalidade)
opcao1.add_command(label= "3 - Funcionalidade Futuramente", command=tfuncionalidade)
opcao1.add_command(label= "4 - Funcionalidade Futuramente", command=qfuncionalidade)

opcao2 = Menu(menu, tearoff=0)
opcao2.add_command(label= "1 - Regra de negócios", command=pregra)
opcao2.add_command(label= "2 - Regra de negócios", command=sregra)
opcao2.add_command(label= "3 - Regra de negócios Futuramente")
opcao2.add_command(label= "4 - Regra de negócios Futuramente")

sobrenos = Menu(menu, tearoff=0)
sobrenos.add_command(label= "Quem somos", command=quemSomos)

sair = Menu(menu, tearoff=0)
sair.add_command(label="Sair", command=exit)


menu.add_cascade(label = "Funcionalidades", menu= opcao1)
menu.add_cascade(label = "Regra de negócios", menu= opcao2)
menu.add_cascade(label = "Sobre Nos", menu= sobrenos)
menu.add_cascade(label = "Sair", menu= sair)


root.mainloop()
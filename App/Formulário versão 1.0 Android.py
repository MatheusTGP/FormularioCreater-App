# Código Feito pôr: MatheusTGamerPro
# GitHub Project © Open-Source
from tkinter import *
import os

di = os.path.dirname('__file__')
arq = di+'Formulario_Android.txt'

def Imprimir ():
	arquivo=open(arq, "a")
	arquivo.write("========================")
	arquivo.write("\n Nome do Enviador: %s"% name.get())
	arquivo.write("\n Para: %s"% para.get())
	arquivo.write("\n Assunto: %s"% assunto.get())
	arquivo.write("\n \n Texto: %s"%texto.get(1.0, END))
	arquivo.write("========================")
	arquivo.close()
	print("Formulário Salvo")

def Close_1 ():
	exit()

Fm = Tk()
Fm.title("Formulário Versão Android")
Fm.geometry("700x650")
Fm.configure(background="black")
Label(Fm, text="Formulário versão Android", background="black",foreground="white").place(x="90",y="10")
texto = Label(Fm, text="Produza um formulário \n com preenchimentos básicos!",background="black",foreground="green").place(x="70",y="60")
Label(Fm, text="Seu Nome: ",background="black",foreground="white").place(x="20",y="160")
name = Entry(Fm,background="gray",foreground="white")
name.place(x="180",y="160")
Label(Fm, text="Para: ",foreground="white",background="black").place(x="20",y="215")
para = Entry(Fm,background="gray",foreground="white")
para.place(x="115",y="215")
Label(Fm, text="Assunto: ",background="black",foreground="white").place(x="20",y="275")
assunto = Entry(Fm, background="gray",foreground="white")
assunto.place(x="150",y="275")
Label(Fm, text="Texto: ",background="black",foreground="white").place(x="18",y="335")
texto = Text(Fm, background="gray",foreground="white")
texto.place(x="125",y="335",width="500",height="250")
Button(Fm, text="Salvar Dados",background="orange",command=Imprimir).place(x="30",y="600",width="280",height="45")
Button(Fm, text="Fechar Formulário",background="orange",command=Close_1).place(x="320",y="600",width="275",height="45")
Fm.mainloop()

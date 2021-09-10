# Code By MatheusTGamerPro
# YouTube: MatheusTGamerPro
# GitHub: github.com/MatheusTGamerPro

from tkinter import *
import os

esc= os.path.dirname("__file__")
nomearq = esc+"Formulario.txt"
def dados():
	arquivo=open(nomearq,"a")
	arquivo.write("Nome: %s"%nm1.get())
	arquivo.write("Senha: %s"%sn1.get())
	arquivo.close()
	
def sair():
	exit()
	
app = Tk()
app.title('Formulario em Python')
app.geometry('500x500')
app.configure(background='#009')

Label(app,text='Nome:',background="#fff",foreground='#009',anchor=W).place(x='10',y='10',width='100',height='30')
nm1 = Entry(app)
nm1.place(x='10',y='45',width='400',height='45')
Label(app,text='Senha:',background='#fff',foreground='#009').place(x='10',y='95',width='100',height='30')
sn1 = Entry(app, text='senha')
sn1.place(x='10',y='130',height='45',width='400')
Button(app, text='Fazer Login',background="#009",foreground="#fff",command=dados).place(x='10',y='185',width='200',height='45')
fechar = Button(app,text="Sair",command=sair).place(x='10',y='240',width='200',height='45')
app.mainloop()

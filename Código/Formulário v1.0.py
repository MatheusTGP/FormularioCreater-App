from tkinter import *
import os

esc=os.path.dirname("__file__")
nomearq= esc+"Formulario.txt"

def CreateArchiver():
    arquivo=open(nomearq,"a")
    arquivo.write("="*30)
    arquivo.write("\n Por: %s "%por.get())
    arquivo.write("\n Para:  %s "%para.get())
    arquivo.write(" \n Assunto:  %s"%resumo.get())
    arquivo.write("\n \n Texto: \n %s"%texto.get("1.0",END))
    arquivo.write("="*30)
    arquivo.close()
    print("Formulario Feito com sucesso, verifique sua pasta do arquivo!" ) 

def close():
    close2=Tk()
    close2.title("Sair")
    close2.geometry("290x120")
    close2.configure(background="red")
    
    Label(close2, text="Voce Realmentemente deseja fechar o formulario?",background="red",foreground="white").place(x="10",y="10")
    fechar=Button(close2, text="Sim",command=finalizar).place(x="40",y="45",width="70",height="30")
    retornar=Button(close2, text="Nao",command=close2.destroy).place(x="160",y="45",width="70",height="30")
    close2.mainloop()
def  finalizar ():
    exit()

app = Tk()
app.title('Formulario em Python V1.0')
app.configure(background='blue')
app.geometry('500x400')

Label(app, text='De:  ',anchor=W,background='blue',foreground='#fff').place(x='10',y='10',width='250',height='25')
por=Entry(app)
por.place(x='10',y='35',width='250',height='25')
Label(app, text='Para: ',anchor=W,foreground='#fff',background='blue').place(x='10',y='65')
para=Entry(app)
para.place(x='10', y='85',width='250',height='25')
Label(app, text="Assunto:  ",anchor=W,foreground="white",background="blue").place(x="10",y="120")
resumo=Entry(app)
resumo.place(x="10",y="140",width="250",height="25")
Label(app, text="Texto:  ", background="blue",foreground="white",anchor=W).place(x="10",y="165")
texto=Text(app)
texto.place(x="10",y="200",width="345",height="150")
Button(app, text='Imprimir Dados',background='black',foreground="white",command=CreateArchiver).place(x='10',y='360')
Button(app, text='Fechar Formulario',background='black',foreground='white',command=close).place(x='120',y='360')

app.mainloop()

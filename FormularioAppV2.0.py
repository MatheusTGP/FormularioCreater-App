from tkinter import *
import os

BAR_DESIGN = "=" * 30
directory = os.path.dirname("__file__")
filename = directory + "Formulario.txt"

def create_file():
    arquivo = open(filename, "a")
    arquivo.write(BAR_DESIGN)
    arquivo.write("\n Por: %s "%por.get())
    arquivo.write("\n Para:  %s "%para.get())
    arquivo.write("\n Assunto:  %s"%resumo.get())
    arquivo.write("\n \n Texto: \n %s"%texto.get("1.0", END))
    arquivo.write(BAR_DESIGN)
    arquivo.close()
    print(f"Formulario produzido com sucesso enviado para {directory}, verifique sua pasta do arquivo." ) 

app = Tk()
app.title('FormularioMaker')
app.configure(background='black')
app.geometry('500x400')

Label(app, text='De: ',anchor=W,background='black', foreground='#fff').place(x="10", y='10', width='250', height='25')
por = Entry(app, background="gray", foreground="white")
por.place(x='10',y='35',width='250',height='25')
Label(app, text='Para: ', anchor=W, foreground='#fff', background='black').place(x='10', y='65')
para = Entry(app, background="gray", foreground="white")
para.place(x='10', y='85',width='250',height='25')
Label(app, text="Assunto: ", anchor=W, foreground="white", background="black").place(x="10", y="120")
resumo=Entry(app, background="gray", foreground="white")
resumo.place(x="10",y="140",width="250",height="25")
Label(app, text="Texto: ", background="black", foreground="white",anchor=W).place(x="10", y="165")
texto = Text(app, background="gray", foreground="white")
texto.place(x="10",y="200",width="345",height="150")
Button(app, text='Salvar Informações', background='#009', foreground="white", command=create_file).place(x='10', y='360')

app.mainloop()

from tkinter import *
import os

BAR_DESIGN = "=" * 30
directory = os.path.dirname("__file__")
filename = directory + "Formulario.txt"

def create_file():
    arquivo = open(filename, "a")
    arquivo.write(BAR_DESIGN)
    arquivo.write("\n Por: %s" %edt_your_email.get())
    arquivo.write("\n Para:  %s" %edt_subject.get())
    arquivo.write("\n Assunto:  %s" %edt_description.get())
    arquivo.write("\n \n Texto: \n%s" %edt_message.get("1.0", END))
    arquivo.write(BAR_DESIGN)
    arquivo.close()
    print(f"Formulario produzido com sucesso, enviado para {directory}.verifique o diretório do arquivo." ) 

app = Tk()
app.title('FormularioMaker')
app.configure(background='black')
app.geometry('500x400')

Label(app, text='De: ',anchor=W,background='black', foreground='#fff').place(x="10", y='10', width='250', height='25')
Label(app, text='Para: ', anchor=W, foreground='#fff', background='black').place(x='10', y='65')
Label(app, text="Assunto: ", anchor=W, foreground="white", background="black").place(x="10", y="120")
Label(app, text="Texto: ", background="black", foreground="white", anchor=W).place(x="10", y="165")
Button(app, text='Salvar Informações', background='#009', foreground="white", command=create_file).place(x='10', y='360')

edt_your_email = Entry(app, background="gray", foreground="white")
edt_subject = Entry(app, background="gray", foreground="white")
edt_description = Entry(app, background="gray", foreground="white")
edt_message = Text(app, background="gray", foreground="white")

edt_your_email.place(x='10',y='35',width='250',height='25')
edt_subject.place(x="10",y="200",width="345",height="150")
edt_description.place(x="10",y="140",width="250",height="25")
edt_message.place(x='10', y='85',width='250',height='25')

app.mainloop()

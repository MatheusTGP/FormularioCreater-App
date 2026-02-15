from tkinter import *
import os

base_dir = os.path.dirname(__file__)
nomearq = os.path.join(base_dir, "Formulario.txt")

def salvar_formulario():
    with open(nomearq, "a", encoding="utf-8") as arquivo:
        arquivo.write("=" * 30)
        arquivo.write(f"\nPor: {por.get()}")
        arquivo.write(f"\nPara: {para.get()}")
        arquivo.write(f"\nAssunto: {resumo.get()}")
        arquivo.write(f"\n\nTexto:\n{texto.get('1.0', END)}")
        arquivo.write("=" * 30 + "\n")

    print("Formulário salvo com sucesso!")
    
def confirmar_saida():
    janela = Toplevel(app)
    janela.title("Sair")
    janela.geometry("300x120")
    janela.configure(bg="red")

    Label(
        janela,
        text="Deseja realmente fechar?",
        bg="red",
        fg="white"
    ).pack(pady=10)

    Button(janela, text="Sim", command=app.destroy).pack(side=LEFT, padx=20, pady=10)
    Button(janela, text="Não", command=janela.destroy).pack(side=RIGHT, padx=20, pady=10)

app = Tk()
app.title("Formulário em Python")
app.configure(bg="blue")
app.geometry("500x400")

Label(app, text="De:", bg="blue", fg="white").place(x=10, y=10)
por = Entry(app)
por.place(x=10, y=35, width=250)

Label(app, text="Para:", bg="blue", fg="white").place(x=10, y=65)
para = Entry(app)
para.place(x=10, y=90, width=250)

Label(app, text="Assunto:", bg="blue", fg="white").place(x=10, y=120)
resumo = Entry(app)
resumo.place(x=10, y=145, width=250)

Label(app, text="Texto:", bg="blue", fg="white").place(x=10, y=175)
texto = Text(app)
texto.place(x=10, y=200, width=350, height=120)

Button(app, text="Salvar", command=salvar_formulario).place(x=10, y=340)
Button(app, text="Fechar", command=confirmar_saida).place(x=100, y=340)

app.mainloop()

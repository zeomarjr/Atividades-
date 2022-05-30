from tkinter import *
# back-end
def imprimir():
    lbl['text'] = inl.get()
    print(in1.get())

# front-end
# window
janela = Tk()

# geometria
janela.geometry('400x300+500+500')
janela.minsize(width=100, height=100)
janela.maxsize(width=900, height=600)

# widgets
lb1 = Label(janela, text='Olá mundo!', font='Arial 26', fg='red')
in1 = Entry(janela, font='Arial 26')
bt1 = Button(janela, text='sair', font='Arial 26', command=quit)
bt2 = Button(janela, text='Imprimir', font='Arial 26', command=imprimir)

# layout
lb1.pack()
in1.pack()
bt1.pack()
bt2.pack()

# run
janela.mainloop()
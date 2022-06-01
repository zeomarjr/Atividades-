from tkinter import *

# back-end
def soma():
    lb1['text']=int(in1.get())+int(in2.get())


# front-end
# window
janela = Tk()

# geometria
janela.geometry('400x300+500+500')
janela.minsize(width=100, height=100)
janela.maxsize(width=900, height=600)

# widgets
lb1 = Label(janela, text='Resultado', font='Arial 26', fg='red')
in1 = Entry(janela, font='Arial 26')
in2 = Entry(janela, font='Arial 26')
bt1 = Button(janela, text='Soma', font='Arial 26', command=soma)

# layout
lb1.pack()
in1.pack()
in2.pack()
bt1.pack()

janela.mainloop()
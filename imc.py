from tkinter import *

#back-end
def IMC():
    lb1['text'] = lb1
    pass

# front-end
# window
janela = Tk()

# geometria
janela.geometry('400x300+500+500')
janela.minsize(width=100, height=100)
janela.maxsize(width=900, height=600)

# widgets
lb1 = Label(janela, text='PESO', font='Arial 26', fg='red')
lb11 = Entry(janela, font='Arial 26')
lb2 = Label(janela, text='ALTURA', font='Arial 26', fg='red')
lb22 = Entry(janela, font='Arial 26')
bt1 = Button(janela, text='IMC', font='Arial 26', command=IMC)

# layout
lb1.grid(row=0, column=0)
lb11.grid(row=0, column=1)
lb2.grid(row=1, column=0)
lb22.grid(row=1, column=1)
bt1.grid(row=2, column=1)

# run
janela.mainloop()

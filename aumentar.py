from tkinter import *

# back-end
def aumentar():
    if lb1['text'] <10:
        lb1['text'] += 1

def diminuir():
    if lb1['text'] >-10:
        lb1['text'] -=1

# front-end
# window
janela = Tk()

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.bind('-', lambda event: diminuir())
janela.bind('+', lambda event: aumentar())

# widgets
lb1 = Label(janela, text=0, font='Arial 26', fg='red')
bt1 = Button(janela, text='+', font='Arial 26', command=aumentar)
bt2 = Button(janela, text='-', font='Arial 26', command=diminuir)

# layout
lb1.grid(row=0, column=1, sticky=NSEW)
bt1.grid(row=0, column=2, sticky=NSEW)
bt2.grid(row=0, column=0, sticky=NSEW)

# run
janela.mainloop()
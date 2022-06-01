from tkinter import *

#back-end
def IMC():
    
    if ent1.get().replace('.','',1) and ent2.get().replace('.','',1):
        x = round(float(ent1.get())/(float(ent2.get())**2),2)
        lb3['text'] = x
        if x < 18.5:
            res['text'] = 'Abaixo do peso :('
        elif x >= 18.5 and x <= 24.9:
            res['text'] = 'Peso ideal :D'
        elif x >= 25.0 and x <= 29.9:
            res['text'] = 'Acima do peso :/'
        elif x >= 30.0 and x <= 39.9:
            res['text'] = 'Obesidade Grau I e II :o'
        elif x > 40:
            res['text'] = 'Obesidade Mórbida :O'

    else:
        lb3['text']='Algo errado, amigo(a)!!'

# front-end
# window
root = Tk()

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.bind('q', lambda event: quit())

# widgets
lb1 = Label(root, text='PESO', font='Arial 26', fg='black')
ent1 = Entry(root, font='Arial 26')
lb2 = Label(root, text='ALTURA', font='Arial 26', fg='black')
ent2 = Entry(root, font='Arial 26')
bt1 = Button(root, text='CALCULAR', font='Arial 26', command=IMC, fg='red')
lb3 = Label(root, text= 0.0, font='Arial 26', fg='blue')
res = Label(root, text='RESULTADO', font='Arial 26', fg='red')

# layout
lb1.grid(row=0, column=0, sticky=NSEW)
ent1.grid(row=0, column=1, sticky=NSEW)
lb2.grid(row=1, column=0, sticky=NSEW)
ent2.grid(row=1, column=1, sticky=NSEW)
bt1.grid(row=2, column=0, columnspan=3, sticky=NSEW)
lb3.grid(row=3, column=0, columnspan=3, sticky=NSEW)
res.grid(row=4, column=0, columnspan=3, sticky=NSEW)

# run
root.mainloop()

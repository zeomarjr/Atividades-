from tkinter import *

#back-end


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

# widgets
lb1 = Label(root, text='C°', font='Arial 26', fg='red')
ent1 = Entry(root, font='Arial 26')
lb2 = Label(root, text='Resultado', font='Arial 26', bg='black', fg='red')
ent2 = Entry(root, font='Arial 26')
lb3 = Label(root, text='F°', font='Arial 26', fg='red')

# layout
lb1.grid(row=0, column=0)
ent1.grid(row=0, column=1, columnspan=1, sticky=NSEW)
lb2.grid(row=2, column=2)
ent2.grid(row=1, column=0)
lb3.grid(row=1, column=1)


# run
root.mainloop()

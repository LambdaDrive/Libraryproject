from tkinter import ttk
from tkinter import *

root = Tk()

frametop = Frame(root)
frametop.pack(side = TOP)

buttonadd = Button(frametop, text = 'Add book')
buttonadd.grid(row = 0, column = 0)

buttonremove = Button(frametop, text = 'Remove a book')
buttonremove.grid(row = 0, column = 1)

buttonchange = Button(frametop, text = 'Update info book')
buttonchange.grid(row = 0, column = 2)

buttonsearch = Button(frametop, text = 'Search')
buttonsearch.grid(row = 0, column = 3)

framedown = Frame(root)
framedown.pack()

lista = ttk.Treeview(framedown, selectmode = 'browse', height = 10, columns = ('Id', 'Title', 'Author'), displaycolumns = '#all')
lista.pack()

if __name__ == '__main__' :
    root.mainloop()

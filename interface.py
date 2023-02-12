from tkinter import ttk
from tkinter import *
import functions

def addbook():
    global entrytitle, entryauthor, newwindow
    
    title = entrytitle.get()
    author = entryauthor.get()
    
    functions.create('biblioteca.db', title, author)

    #insira codigo para mostrar livros aqui

    newwindow.quit()

def openaddwindow():

    newwindow = Toplevel(root)

    newwindow.title("Add book")

    Label(newwindow, text = "Title").grid(row = 0, column = 0)
    
    entrytitle = Entry(newwindow)
    entrytitle.grid(row = 0,column = 1)
    
    Label(newwindow, text = "Author:").grid(row = 1, column = 0)
    
    entryauthor = Entry(newwindow)
    entryauthor.grid(row = 1, column = 1)

    buttonok = Button(newwindow, text = "OK", command = addbook)
    buttonok.grid(row = 2, column = 0)
    
    buttoncancel = Button(newwindow, text = "Cancel", command = newwindow.quit())
    buttoncancel.grid(row = 2, column = 1)

def removebookwindow():

    newwindow = Toplevel(root)

    Label(newwindow, text = 'Book id:').grid(row = 0, column = 0)

    entrybookid = Entry(newwindow)
    entrybookid.grid(row = 0, column = 1)

    buttonok = Button(newwindow, text = 'OK')
    buttonok.grid(row = 1,column = 0)

    buttoncancel = Button(newwindow, text = 'Cancel', command = newwindow.quit())
    buttoncancel.grid(row = 1, column = 1)

def updatebookwindow():

    newwindow = Toplevel(root)

    Label(newwindow, text = 'Book id:').grid(row = 0, column = 0)
    
    entryid = Entry(newwindow)
    entryid.grid(row = 0, column = 1)
    
    Label(newwindow, text = 'Title:').grid(row = 1, column = 0)

    entrytitle = Entry(newwindow)
    entrytitle.grid(row = 1, column = 1)

    Label(newwindow, text = 'Author:').grid(row = 2, column = 0)

    entryauthor = Entry(newwindow)
    entryauthor.grid(row = 2, column = 1)

    buttonok = Button(newwindow, text = 'OK')
    buttonok.grid(row = 3, column = 0)

    buttoncancel = Button(newwindow, text = 'Cancel', command = newwindow.quit())
    buttoncancel.grid(row = 3, column = 1)


root = Tk()

frametop = Frame(root)
frametop.pack(side = TOP)

buttonadd = Button(frametop, text = 'Add book', command = openaddwindow)
buttonadd.grid(row = 0, column = 0)

buttonremove = Button(frametop, text = 'Remove a book', command = removebookwindow)
buttonremove.grid(row = 0, column = 1)

buttonchange = Button(frametop, text = 'Update book info', command = updatebookwindow)
buttonchange.grid(row = 0, column = 2)

framedown = Frame(root)
framedown.pack()

lista = ttk.Treeview(framedown, selectmode = 'browse', height = 10, columns = ('Id', 'Title', 'Author'), displaycolumns = '#all')
lista.pack()

if __name__ == '__main__' :
    root.mainloop()

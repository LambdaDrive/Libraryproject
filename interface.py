from tkinter import ttk
from tkinter import *
import functions

def addbook():
    global title, author
    
    if title.get() == '' and author.get == '':
        pass
    else:
        functions.create('biblioteca.db', title.get(), author.get())
        
        refreshtreeview()

def removebook():

    global cod

    if cod.get() == 0:
        pass
    else:
        functions.delete('biblioteca.db', cod.get())

        refreshtreeview()

def updatebook():

    global title, author, cod
    
    if title.get() == '' and author.get() == '' and cod.get() == 0:
        pass
    else:
        functions.update('biblioteca.db', cod.get(), title.get(), author.get())

        refreshtreeview()

    
def variableaddbook(titleentry, authorentry, janela):

    global title, author

    title.set(titleentry.get())
    author.set(authorentry.get())
    
    addbook()
    
    janela.destroy()

def variableremovebook(entrycod, janela):

    global cod

    cod.set(entrycod.get())
    
    removebook()

    janela.destroy()

def variableupdatebook(entrycod, entrytitle, entryauthor, janela):

    global title, author, cod

    cod.set(entrycod.get())
    title.set(entrytitle.get())
    author.set(entryauthor.get())

    updatebook()

    janela.destroy()

def refreshtreeview():

    global lista

    for item in lista.get_children():
        lista.delete(item)

    livros = functions.read('biblioteca.db')

    for livro in livros:
        lista.insert('', END, values = livro)

def openaddwindow():

    newwindow = Toplevel(root)

    newwindow.title("Add book")

    Label(newwindow, text = "Title").grid(row = 0, column = 0)
    
    entrytitle = Entry(newwindow)
    entrytitle.grid(row = 0,column = 1)
    
    Label(newwindow, text = "Author:").grid(row = 1, column = 0)
    
    entryauthor = Entry(newwindow)
    entryauthor.grid(row = 1, column = 1)

    buttonok = Button(newwindow, text = "OK", command = lambda:variableaddbook(entrytitle, entryauthor, newwindow))
    buttonok.grid(row = 2, column = 0)
    
    buttoncancel = Button(newwindow, text = "Cancel", command = newwindow.destroy)
    buttoncancel.grid(row = 2, column = 1)

def removebookwindow():

    newwindow = Toplevel(root)

    Label(newwindow, text = 'Book id:').grid(row = 0, column = 0)

    entrybookid = Entry(newwindow)
    entrybookid.grid(row = 0, column = 1)

    buttonok = Button(newwindow, text = 'OK', command = lambda: variableremovebook(entrybookid, newwindow))
    buttonok.grid(row = 1,column = 0)

    buttoncancel = Button(newwindow, text = 'Cancel', command = newwindow.destroy)
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

    buttonok = Button(newwindow, text = 'OK', command = lambda:variableupdatebook(entryid, entrytitle, entryauthor, newwindow))
    buttonok.grid(row = 3, column = 0)

    buttoncancel = Button(newwindow, text = 'Cancel', command = newwindow.destroy)
    buttoncancel.grid(row = 3, column = 1)

functions.initializedb('biblioteca.db')

root = Tk()

title = StringVar()
author = StringVar()
cod = IntVar()

frametop = Frame(root)
frametop.pack(side = TOP)

buttonadd = Button(frametop, text = 'Add book', command = openaddwindow)
buttonadd.grid(row = 0, column = 0)

buttonremove = Button(frametop, text = 'Remove a book', command = removebookwindow)
buttonremove.grid(row = 0, column = 1)

buttonchange = Button(frametop, text = 'Update book info', command = updatebookwindow)
buttonchange.grid(row = 0, column = 2)

buttonexit = Button(frametop, text = 'Exit', command = root.destroy)
buttonexit.grid(row = 0, column = 3)

framedown = Frame(root)
framedown.pack()

lista = ttk.Treeview(framedown, selectmode = 'browse', height = 10, columns = ('id', 'title', 'author'), show='headings')

lista.heading('id', text = 'Id')
lista.heading('title', text = 'Title')
lista.heading('author', text = 'Author')

livrostreeview = functions.read('biblioteca.db')

for livro in livrostreeview:
    lista.insert('', END, values = livro)

lista.pack()

if __name__ == '__main__' :
    root.mainloop()

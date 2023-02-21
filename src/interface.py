from tkinter import ttk
from tkinter import *
import functions

def addbook():
    
    global title, author #import tkinter variable to control title and author
    
    if title.get() == '' and author.get == '':#test if variables are initialized
        pass
    else:
        functions.create('biblioteca.db', title.get(), author.get())#run the function to save info to database
        
        refreshtreeview()#refresh the treeview with the new info

def removebook():

    global cod #import tkinter varible to control the book id

    if cod.get() == 0:#test if the variable is initialized
        pass
    else:
        functions.delete('biblioteca.db', cod.get())#run the function to remove book in the database

        refreshtreeview() #refresh the treeview with the new info

def updatebook():

    global title, author, cod #import the tkinter variables that control the title, author and bookid
    
    if title.get() == '' and author.get() == '' and cod.get() == 0: #test if the variables are initialized
        pass
    else:
        functions.update('biblioteca.db', cod.get(), title.get(), author.get()) #update the entry with code of cod variable and change the title and author of the book in the database

        refreshtreeview() #refresh the treeview with the new info

    
def variableaddbook(titleentry, authorentry, janela):

    global title, author #load title and author variables to update values

    title.set(titleentry.get()) #set variable with data from the title window entry
    author.set(authorentry.get()) #set variable with data from the author window entry
    
    addbook() #run the function to save data to the database
    
    janela.destroy() #close the window

def variableremovebook(entrycod, janela):

    global cod #load bookid variable to update the value

    cod.set(entrycod.get()) #set bookid variable with data from the window id entry
    
    removebook() #run the function to save the data to the database

    janela.destroy() #close the window

def variableupdatebook(entrycod, entrytitle, entryauthor, janela):

    global title, author, cod #load tkinter variables to update the values
    
    #set id, title and author variables with values from the entries
    cod.set(entrycod.get())
    title.set(entrytitle.get())
    author.set(entryauthor.get())

    updatebook() #run the function to save the data to the database

    janela.destroy() #close the window

def refreshtreeview():

    global lista #load treeview

    for item in lista.get_children():
        lista.delete(item) #clear all the data from treeview

    livros = functions.read('biblioteca.db') #load the list of books from the database

    for livro in livros:
        lista.insert('', END, values = livro) #insert the books in treeview

def openaddwindow():
    #Create a window to add books to the database as a popup window
    newwindow = Toplevel(root) 

    newwindow.title("Add book")

    Label(newwindow, text = "Title").grid(row = 0, column = 0)
    
    entrytitle = Entry(newwindow)
    entrytitle.grid(row = 0,column = 1)
    
    Label(newwindow, text = "Author:").grid(row = 1, column = 0)
    
    entryauthor = Entry(newwindow) 
    entryauthor.grid(row = 1, column = 1)

    buttonok = Button(newwindow, text = "OK", command = lambda:variableaddbook(entrytitle, entryauthor, newwindow)) #lambda command to user input in the function
    buttonok.grid(row = 2, column = 0)
    
    buttoncancel = Button(newwindow, text = "Cancel", command = newwindow.destroy) #button to close the window
    buttoncancel.grid(row = 2, column = 1)

def removebookwindow():
    #Create a window to remove books 
    newwindow = Toplevel(root)

    Label(newwindow, text = 'Book id:').grid(row = 0, column = 0)

    entrybookid = Entry(newwindow)
    entrybookid.grid(row = 0, column = 1)

    buttonok = Button(newwindow, text = 'OK', command = lambda: variableremovebook(entrybookid, newwindow))
    buttonok.grid(row = 1,column = 0)

    buttoncancel = Button(newwindow, text = 'Cancel', command = newwindow.destroy)
    buttoncancel.grid(row = 1, column = 1)

def updatebookwindow():
    #Create a window to update book info based on book id
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

functions.initializedb('biblioteca.db') #Initialize the database

#Create the main window
root = Tk()
#Initilize the tkinter variables to control the title, author and id
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

livrostreeview = functions.read('biblioteca.db')#Load book data from the database to put into the treeview

for livro in livrostreeview:    #Insert database data into treeview
    lista.insert('', END, values = livro)

lista.pack()

if __name__ == '__main__' :
    #Run main window
    root.mainloop()


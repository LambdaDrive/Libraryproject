import sqlite3

def initializedb(dbname):
    #Function to initialize database    
    con = sqlite3.connect(dbname)   #Open connection with database
    cur = con.cursor() #Create a cursor

    cur.execute("CREATE TABLE IF NOT EXISTS livros(cod INTEGER PRIMARY KEY, titulo varchar(20) NOT NULL, autor varchar(20) NOT NULL)") #Create the table if it not exists
    
    con.commit() #Commit the changes

    con.close() #Close the connection

def create(dbname, titulo, autor):
    #Function to add info ot the database
    con = sqlite3.connect(dbname)
    
    cur = con.cursor()
    
    data = (titulo, autor)

    cur.execute("""
    INSERT INTO livros (titulo, autor) VALUES (?,?)""", data)

    con.commit()

    con.close()

def read(dbname):
    #Function to read from the database
    con = sqlite3.connect(dbname)

    cur = con.cursor()

    res = cur.execute("SELECT * FROM livros")
    livros = res.fetchall()

    con.close()

    return livros

def update(dbname, cod, titulo, autor):
    #Function to update info of the database
    con = sqlite3.connect(dbname)

    cur = con.cursor()
    
    params = (titulo, autor, cod)

    cur.execute("UPDATE livros SET titulo = ?, autor = ? WHERE cod = ?", params)
    
    con.commit()

    con.close()

def delete(dbname, cod):
    #Function to delete an entry in the database
    con = sqlite3.connect(dbname)

    cur = con.cursor()

    params = (cod,)

    cur.execute("DELETE FROM livros WHERE cod = ?", params)

    con.commit()

    con.close()


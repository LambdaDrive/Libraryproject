import sqlite3

dbname = "biblioteca.db"

def initializedb(dbname):
    
    con = sqlite3.connect(dbname)
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS livros(cod INTEGER PRIMARY KEY, titulo varchar(20) NOT NULL, autor varchar(20) NOT NULL)")
    
    con.close()

def create(dbname, titulo, autor):
    
    con = sqlite3.connect(dbname)
    
    cur = con.cursor()
    
    data = (titulo, autor)

    cur.execute("""
    INSERT INTO livros (titulo, autor) VALUES (?,?)""", data)

    con.commit()

    con.close()

def read(dbname):

    con = sqlite3.connect(dbname)

    cur = con.cursor()

    res = cur.execute("SELECT * FROM livros")
    livros = res.fetchall()

    con.close()

    return livros

def update(dbname, cod, titulo, autor):

    con = sqlite3.connect(dbname)

    cur = con.cursor()
    
    params = (titulo, autor, cod)

    cur.execute("UPDATE livros SET titulo = ?, autor = ? WHERE cod = ?", params)
    
    con.commit()

    con.close()

def delete(dbname, cod):

    con = sqlite3.connect(dbname)

    cur = con.cursor()

    params = (cod,)

    cur.execute("DELETE FROM livros WHERE cod = ?", params)

    con.commit()

    con.close()


import sqlite3

DB_NAME = 'dbTeste.sqlite'

def conectaDB():
    try:
        conn = sqlite3.connect(DB_NAME)
        print("DB conectado...")
        return conn
    except:
        return "Houve um erro na conexão com o banco de dados."

def selecionaTodosUsuarios():
    conn = conectaDB()
    cur = conn.cursor()
    query = 'SELECT * from users'
    cur.execute(query)
    res = cur.fetchall()
    return res
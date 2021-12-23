from logging import log
import sqlite3
import hashlib

DB_NAME = 'dbTeste.sqlite'

def conectaDB():
    try:
        conn = sqlite3.connect(DB_NAME)
        print("DB conectado...")
        return conn
    except:
        return "Houve um erro na conexão com o banco de dados."

def selecionaTodosUsuarios():
    try:
        conn = conectaDB()
        cur = conn.cursor()
        query = 'SELECT * from users'
        cur.execute(query)
        res = cur.fetchall()
        conn.close()
        return res
    except:
        return "Houve um erro ao consultar o banco de dados."

def addUsuario(login, email, senha):
    try:
        conn = conectaDB()
        cur = conn.cursor()
        if checkLoginUnico(login) == True:
            query = 'INSERT INTO users (login, email, senha) VALUES (?, ?, ?)'
            cur.execute(query, [login, email, senha])
            conn.commit()
            conn.close()
            return True
        else:
            return False
    except:
        return "Houve um erro ao adicionar um usuário ao banco de dados."

def deleteUsuario(id):
    try:
        conn = conectaDB()
        cur = conn.cursor()
        query = 'DELETE FROM users where id=?'
        cur.execute(query,[id])
        conn.commit()
        conn.close()
        return True
    except:
        return "Houve um erro ao deletar um usuário do banco de dados."

def selectUsuario(id):
    try:
        conn = conectaDB()
        cur = conn.cursor()
        query = 'SELECT * from users where id=?'
        cur.execute(query, [id])
        res = cur.fetchone()
        conn.close()
        return res
    except:
        return "Houve um erro ao selecionar o usuario no banco de dados."
    
def updateUsuario(id, login, email, senha):
    try:
        conn = conectaDB()
        cur = conn.cursor()
        if checkLoginUnico(login) == True:
            query = 'UPDATE users SET login=?, email=?, senha=? where id=?'
            cur.execute(query, [login, email, senha, id])
            conn.commit()
            conn.close()
            return True
        else:
            return False
    except:
        return "Houve um erro ao editar o usuario no banco de dados."

def checkLoginUnico(login):
        conn = conectaDB()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM users WHERE login='{0}'".format(login))
        numIguais = cur.fetchone()[0]
        if numIguais == 0:
            return True
        else:
            return False
    
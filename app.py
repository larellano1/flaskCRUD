##### Code inspired from video by Cairocoders https://www.youtube.com/watch?v=z3109C_xDP8
##### If you're going to use this code for a user table, don't forget to encrypt the passwords!

from flask import Flask, render_template, redirect, request, url_for, flash
import myFuncs

app = Flask(__name__)

##Página de entrada para ver a tabela de usuarios.
@app.route('/')
def index():
    res = myFuncs.selecionaTodosUsuarios()
    return render_template('index.html', lista_usuarios = res)

##Método para adicionar usuário.
@app.route('/addUser', methods=['POST'])
def addUser():
    if request.method == 'POST':
        login = request.form['flogin']
        email = request.form['femail']
        senha = request.form['fpass']
        res = myFuncs.addUsuario(login, email, senha)
        print(res)
        if res == True:
            flash("Usuário adicionado com sucesso.")
            return redirect(url_for('index'))
        elif res == False:
            flash("Login já em uso. Favor escolher outro.")
            return redirect(url_for('index'))
        else:
            flash("Houve um erro na operação addUser.")
            return redirect(url_for('index'))

##Método para deletar usuário.
@app.route('/delete/<id>', methods=['GET'])
def deleteUsuario(id):
    if request.method =='GET':
        if myFuncs.deleteUsuario(id) == True:
            flash("Usuário deletado com sucesso.")
            return redirect(url_for('index'))
        else:
            flash("Houve um erro na operação deleteUser.")
            return redirect(url_for('index'))

##Método para exibir formulário para editar usuário.
@app.route('/edit/<id>', methods=['POST', 'GET'])
def editUsuario(id):
    user = myFuncs.selectUsuario(id)
    return render_template('edit.html', user = user)

##Método para editar usuário.
@app.route('/update/<id>', methods=['POST', 'GET'])
def updateUsuario(id):
     if request.method == 'POST':
        login = request.form['flogin']
        email = request.form['femail']
        senha = request.form['fpass']
        res = myFuncs.updateUsuario(id, login, email, senha)
        if res == True:
            flash("Usuário editado com sucesso.")
            return redirect(url_for('index'))
        elif res == False:
            flash("Login já em uso. Favor escolher outro.")
            return redirect(url_for('index'))
        else:
            flash("Houve um erro na operação UpdateUser.")
            return redirect(url_for('index'))

##Método main para rodar app.
if __name__ == '__main__':
    app.secret_key = 'secret'
    app.run(debug=True)
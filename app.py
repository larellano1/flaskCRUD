from flask import Flask, render_template
import myFuncs

app = Flask(__name__)

@app.route('/')
def index():
    res = myFuncs.selecionaTodosUsuarios()
    print(res)
    return render_template('index.html', lista_usuarios = res)

if __name__ == '__main__':
    app.run(debug=True)
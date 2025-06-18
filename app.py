from flask import *
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash

from database import produtos, carrinho, usuarios

app = Flask(__name__)

app.secret_key = 'bfb07264b99b8cd48a50720720dc0666adabc601ec82f5a557317e480ed080d2'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'

Session(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/cadastro", methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['login']
        email = request.form['email']
        if email in usuarios.keys():
            return redirect(url_for('cadastro'))
        else:
            senha = request.form['senha']
            senha = generate_password_hash(senha)
            usuarios[email] = [senha, nome]
            return redirect(url_for('login'))
    else:
        return render_template('cadastro.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if email in usuarios:
            if check_password_hash(usuarios[email][0], senha):
                return redirect(url_for('rota_produtos'))
            else:
                return redirect(url_for('login'))
        else: 
            return redirect(url_for('cadastro'))
    return render_template('login.html')

@app.route("/logout")
def logout():
    return redirect(url_for('index'))
 
@app.route("/produtos", methods=['POST','GET'])
def rota_produtos():
    return render_template('produtos.html', produtos=produtos)

@app.route("/carrinho", methods=['POST','GET'])
def rota_carrinho():

    if request.method == 'POST':
        pass #eventualmente o request
    return render_template('carrinho.html', carrinho=carrinho)

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os


from database import products, users, dump_database
from models import User

if not os.path.exists('./.env'):
    from secrets import token_hex

    with open('./.env', 'w') as fw:
        fw.write(f'SECRET_KEY = "{token_hex()}" ') 

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') # gera uma nova key toda vez que reiniciar o servidor

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        user_data = users[user_id]
        return User(user_id, user_data)
    else:
        return None

@app.route('/')
def index():
    # v SE QUISER QUE A SESSÃO FIQUE DEPOIS DE FECHAR O NAVEGADOR v
    # session.permanent = True

    return render_template('index.html')

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['login']
        email = request.form['email']
        password_hash = generate_password_hash(request.form['senha'])
        if email not in users.keys():
            id = str(len(users) + 1) # auto increment
            users[id] = {'username':username, 'email':email, 'password_hash':password_hash} # adiciona ao banco de dados
            dump_database('user')
            # print(users)
            return redirect(url_for('login'))
    else:
        return render_template('cadastro.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['senha']

        for id, data in users.items(): # INEFICIENTE, QUANDO INTEGRAR COM BANCO DE DADOS HAVERÁ A CONSULTA COM WHERE
            # NÃO SE USA FLASK LOGIN E SESSION AO MESMO TEMPO EM AUTENTICAÇÃO

            # print(id)
            # print(data)
            if data['email'] == email:
                if check_password_hash(users[id]['password_hash'], password):
                    login_user(User(id, data))
                    # print(current_user.is_authenticated)
                    
                    return redirect(url_for('index'))
                else:
                    flash('Senha incorreta', category='error')
                    return redirect(url_for('login'))
        # usuário não cadastrado
        return redirect(url_for('cadastro')) 
    if request.method == 'GET': # não precisava desse IF, porém deixa mais legível
        return render_template('login.html')

@app.route("/logout")
def logout():
    logout_user()

    return redirect(url_for('index'))

@app.route("/produtos", methods=['POST','GET'])
@login_required
def produtos():
    return render_template('produtos.html', products=products)

@app.route("/carrinho", methods=['POST','GET'])
@login_required
def carrinho():
    if request.method == 'POST':
        pass # eventualmente o request
    cart = {}
    return render_template('carrinho.html', cart=cart)

if __name__ == '__main__':
    app.run(debug=True)
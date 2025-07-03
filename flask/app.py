from flask import *
from werkzeug.security import generate_password_hash, check_password_hash

from database import products, wallet, users

app = Flask(__name__)

app.secret_key = 'bfb07264b99b8cd48a50720720dc0666adabc601ec82f5a557317e480ed080d2'

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
        password = request.form['senha']
        password = generate_password_hash(password)
        if email not in users.keys():
        #     return redirect(url_for('cadastro'))
        # else:
            
            users[email] = {'username':username, 'password': password}
            print(users)
            return redirect(url_for('login'))
    else:
        return render_template('cadastro.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['senha']
        if email in users:
            if check_password_hash(users[email]['password'], password):
                print('Logou')
                session['user'] = email
                session['password'] = generate_password_hash(password)
                print(session)
                return redirect(url_for('rota_produtos'))
            else:
                print('Senha errada')
                return redirect(url_for('login'))
        else: 
            return redirect(url_for('cadastro'))
    return render_template('login.html')

@app.route("/logout")
def logout():
    return redirect(url_for('index'))
 
@app.route("/produtos", methods=['POST','GET'])
def rota_produtos():
    return render_template('produtos.html', produtos=products)

@app.route("/carrinho", methods=['POST','GET'])
def rota_carrinho():

    if request.method == 'POST':
        pass #eventualmente o request
    return render_template('carrinho.html', carrinho=wallet)

if __name__ == '__main__':
    app.run(debug=True)


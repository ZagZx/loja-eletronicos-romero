from flask import *

app = Flask(__name__)

usrs = {'adm': 'admadm'} #Usuários

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/cadastro", methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        usr = request.form['login']
        if usr in usrs.keys():
            return redirect(url_for('cadastro'))
        else:
            sen = request.form['senha']
            usrs[usr] = sen
            return redirect(url_for('login'))
    else:
        return render_template('cadastro.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/logout")
def logout():
    pass

@app.route("/produtos")
def produtos():
    return render_template('produtos.html')

@app.route("/carrinho")
def carrinho():
    return render_template('carrinho.html')


if __name__ == '__main__':
    app.run(debug=True)


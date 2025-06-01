from flask import *
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash

from database.produtos import LISTA_PRODUTOS, carrinho, usuarios

app = Flask(__name__)

app.secret_key = 's69LFQk4eGAeHXRk7QfPRc6fspnJMCH7muRhL^PGcuu@82k&oNgH6Cj9wKYZpGBMZGc!Wo9ZoMUTY#ZKqAUY%YDX@GXnqdix59DM7ZCSbXiydj$4ezA4s75UmgFz2beMd9J!DoZvMsA4zqx6rQV96#HkeyEaF$8u#VuTx8MStrG@jVkuKaSHAdF$C2ybd^LGM34WGja2njvDBg4vTAaybnbMU8Gwu@fKn7Nt&%uP%GCrgU$M$brwB5NR72hc&@YzZNd3ekww6W&yn7QUp%KD3QtsLf6qbmcUz^C23ZqnifKmb!8oF5GRNhA7n5d2D!NVaSWo#XMMDcKMuF3fz@N#gUyENcYfmut67QwKdxrKTX5QK8YtoeiepEYnBX&X$mWqEibaMS%DTGGphDBxXuCbQG^fGNN3Prtpj9q$Adr5uMzu#tzNpLuJM2haEMyniehsQ8!tzdAgA&6TSRPYkaE3Da!mS3APicap3pxKjL5tHPXD&QdBi8Et7mNu8p#ik'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'

# Session(app)

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
                session['name'] = usuarios[email][1]
                return redirect(url_for('produtos'))
            else:
                return redirect(url_for('login'))
        else: 
            return redirect(url_for('cadastro'))
    return render_template('login.html')

@app.route("/logout")
def logout():
    session['name'] = None
    return redirect(url_for('index'))
 
@app.route("/produtos", methods=['POST','GET'])
def produtos():
    return render_template('produtos.html', produtos=LISTA_PRODUTOS)

@app.route("/carrinho", methods=['POST','GET'])
def carrinho():
    carrinho[session['name']]
    if request.method == 'POST':
        pass #eventualmente o request
    return render_template('carrinho.html', carrinho=carrinho)

if __name__ == '__main__':
    app.run(debug=True)


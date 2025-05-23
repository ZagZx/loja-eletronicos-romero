from flask import *

app = Flask(__name__)

app.secret_key = 's69LFQk4eGAeHXRk7QfPRc6fspnJMCH7muRhL^PGcuu@82k&oNgH6Cj9wKYZpGBMZGc!Wo9ZoMUTY#ZKqAUY%YDX@GXnqdix59DM7ZCSbXiydj$4ezA4s75UmgFz2beMd9J!DoZvMsA4zqx6rQV96#HkeyEaF$8u#VuTx8MStrG@jVkuKaSHAdF$C2ybd^LGM34WGja2njvDBg4vTAaybnbMU8Gwu@fKn7Nt&%uP%GCrgU$M$brwB5NR72hc&@YzZNd3ekww6W&yn7QUp%KD3QtsLf6qbmcUz^C23ZqnifKmb!8oF5GRNhA7n5d2D!NVaSWo#XMMDcKMuF3fz@N#gUyENcYfmut67QwKdxrKTX5QK8YtoeiepEYnBX&X$mWqEibaMS%DTGGphDBxXuCbQG^fGNN3Prtpj9q$Adr5uMzu#tzNpLuJM2h%aEMyniehsQ8!tzdAgA&6TSRPYkaE3Da!mS3APicap3p%xKjL5tHPXD&QdBi8Et7mNu8p#ik'

usrs = {'adm': 'admadm'} #Usuários
LISTA_PRODUTOS = [
    ['Mouse', 30.00],
    ['Teclado', 100.00],
    ['Microfone', 500.00],
    ['Headset', 400.00],
    ['Mesa digitalizadora', 220.00],
    ['Monitor', 550.00],
    ['impressora', 300.00],
    ['Caixa de som', 120.00],
]

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


           
@app.route("/produtos", methods=['POST','GET'])
def produtos():
    return render_template('produtos.html', produtos=LISTA_PRODUTOS)



@app.route("/carrinho", methods=['POST','GET'])
def carrinho():
    return render_template('carrinho.html')


if __name__ == '__main__':
    app.run(debug=True)


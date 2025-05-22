from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/cadastro", methods=['POST', 'GET'])
def cadastro():
    return render_template('cadastro.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/logout")
def logout():
    pass

produtos = [
            ['mouse', 30.00],
            ['teclado', 100.00],
            ['microfone', 500.00],
            ['fone', 400.00]
           ]
           
@app.route("/produtos")
def produtos():
    return render_template('produtos.html')



@app.route("/carrinho")
def carrinho():
    return render_template('carrinho.html')


if __name__ == '__main__':
    app.run(debug=True)


# Loja de Eletrônicos

Projeto da matéria de Programação de Sistemas para Internet, consiste em uma loja online com a possibilidade de adicionar itens a um carrinho, o projeto deve utilizar Flask, deve ter cookies e session. 

## Docker
### Construindo a imagem
``` bash
docker build -t flask-app ./flask
```

### Rodando a imagem
Se quiser exibir o terminal:
``` bash
docker run -p 5000:5000 flask-app
```
Se quiser o terminal oculto:
``` bash
docker run -dp 5000:5000 flask-app
```
### Servidor está rodando, e agora?
É possível acessar a aplicação de duas formas, com localhost ou com o ip da sua máquina. **Pessoas na mesma rede que você podem acessar a aplicação através do IP da sua máquina.**

#### localhost: 
Para acessar com localhost basta digitar um dos endereços abaixo 
- localhost:5000
- 127.0.0.1:5000

#### ip:
Para acessar pelo ip da sua máquina, primeiro é necessário descobrir o mesmo.

**Windows:** ipconfig  
**Linux:** ip addr

Agora com o ip da máquina em mãos, basta digitar o ip da máquina seguido de dois pontos e a porta, que no caso é 5000.
- ip-da-maquina:5000


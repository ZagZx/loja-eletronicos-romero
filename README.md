# Loja de Eletrônicos

Projeto da matéria de Programação de Sistemas para Internet, consiste em uma loja online com a possibilidade de adicionar itens a um carrinho.

## Requisitos
- Python **OU** Docker

## Tecnologias Utilizadas
- Python
- HTML, CSS, JavaScript
- Framework Flask
- MySQL (Em Breve)
- Docker (opcional)

## Rodando com Python
<details>
  <summary>Windows</summary>

  **IMPORTANTE:** Utilize o CMD/Prompt de Comando, no PowerShell não irá funcionar

  1. Crie o ambiente virtual:
     ```bash
     python -m venv env
     ```

  2. Ative o ambiente virtual:
     ```bash
     .\env\Scripts\activate
     ```
  3. Se dirija à pasta do flask:
     ```bash
     cd .\flask
     ```
  4. Instale os requisitos:
     ```bash
     pip install -r requirements.txt
     ```
  5. Rode o servidor:
     ```bash
     flask run --host 0.0.0.0
     ```

</details>

<details>
  <summary>Linux</summary>

  1. Crie o ambiente virtual:
     ```bash
     python3 -m venv env
     ```

  2. Ative o ambiente virtual:
     ```bash
     source ./env/bin/activate
     ```
  3. Se dirija à pasta do flask:
     ```bash
     cd ./flask
     ```
  4. Instale os requisitos:
     ```bash
     pip install -r requirements.txt
     ```
  5. Rode o servidor:
     ```bash
     flask run --host 0.0.0.0
     ```
</details>

## Rodando com Docker
<details>
  <summary>Iniciando o servidor</summary>

  ### Construindo a imagem
  Na pasta raiz do repositório utilize o seguinte comando:
  ``` bash
  docker build -t flask-app ./flask
  ```
  
  ### Rodando a imagem
  Se quiser exibir o terminal:
  ``` bash
  docker run -p 5000:5000 flask-app
  ```
  **OU** se preferir o terminal oculto:
  ``` bash
  docker run -dp 5000:5000 flask-app
  ```

</details>

<details>
  <summary>Finalizando o servidor</summary>
  
  1. Obtenha o ID do container, procure pela imagem flask-app e copie seu CONTAINER ID:
     ```bash
     docker ps
     ```

  2. Pare o container:
     ```bash
     docker stop (CONTAINER ID aqui)
     ```


</details>

## Servidor está rodando, e agora?
É possível acessar a aplicação de duas formas, com localhost ou com o ip da sua máquina. **Pessoas na mesma rede que você podem acessar a aplicação através do IP da sua máquina.**

- localhost: 
    Para acessar com localhost basta digitar um dos endereços abaixo .
    - localhost:5000
    - 127.0.0.1:5000

- ip:
    1. Descubra o ip ***da sua máquina***
        - Windows 
            ```bash 
            ipconfig
            ```
             
        - Linux: 
            ```bash
            ip addr
            ```
    2. Agora com o ip da máquina em mãos, basta digitar o ip da máquina seguido de dois pontos e a porta, que no caso é 5000.
        - ip-da-maquina:5000


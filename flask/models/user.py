from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id:int, data: dict):
        self.id:int = id # inteiro porque é assim que vem do banco de dados
        self.username:str = data['username']
        self.password_hash:str = data['password_hash']
    
    def get_id(self):
        return str(self.id) # converte para string porque o Flask obriga a fazer isso
    
        
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id:str, data: dict):
        self.id = id
        self.username:str = data['username']
        self.password_hash:str = data['password_hash']

        
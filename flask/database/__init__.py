import json
import os
from typing import Literal

# Obtém o diretório atual do arquivo (database/) | obrigado deepseek
current_dir = os.path.dirname(os.path.abspath(__file__))

# Caminhos completos para os arquivos JSON | obrigado deepseek
users_path = os.path.join(current_dir, 'user.json')
products_path = os.path.join(current_dir, 'product.json')


with open(users_path) as fr:
    users:dict[str,dict[str, str]] = json.load(fr) 

with open(products_path) as fr:
    products:dict[str,float] = json.load(fr) 

def dump_database(database_name:Literal['user', 'product']): #, data: dict):
    if database_name in ['user', 'product']:
        path = ''
        data = {}
        match database_name:
            case 'product':
                path = products_path
                data = products
            case 'user':
                path = users_path
                data = users
        if path:
            with open(path, 'w') as fw:
                json.dump(data, fw, indent = 4)
                
from sqlalchemy import create_engine, URL

url_db = URL.create(
    drivername='mysql',
    username='root',
    host='localhost',
    port=3306
    # database='eletronicos'
)

engine = create_engine(url= url_db)

print(engine)
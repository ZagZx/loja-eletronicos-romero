import sqlite3

with open('./sql/create.sql') as sql_read:
    sqlite3.connect(sql_read)
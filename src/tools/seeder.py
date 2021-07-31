import pymysql.cursors as cursor
import pymysql
from dotenv import load_dotenv
import os
load_dotenv() 

conexion = pymysql.connect(
    host="localhost",
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWD"),
    database=os.getenv("DB_NAME"),
    cursorclass=cursor.DictCursor
)
with conexion:
    with conexion.cursor() as con:
        sql = "INSERT INTO actor (nombre) VALUES (prueba)"
        con.execute(sql,('webmaster@python.org', 'very-secret'))
    conexion.commit()
    
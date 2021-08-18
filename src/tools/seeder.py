import mysql.connector as sql
from dotenv import load_dotenv
import os
load_dotenv() 
conexion = sql.connect(
    host="localhost",
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWD"),
    database=os.getenv("DB_NAME")
)
a = conexion.cursor()
a.execute("SELECT ID FROM punto WHERE nombre='punto1'")
print(a.fetchone())
#conexion.commit()
    
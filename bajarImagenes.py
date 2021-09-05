import os
from dotenv import load_dotenv
import mysql.connector as sql
load_dotenv()
rootPath= os.getenv("PROJECT_PATH")
from src.components.spiders import elespectador
import time
conexion = sql.connect(
    host="localhost",
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWD"),
    database=os.getenv("DB_NAME"),
)
query = "SELECT DISTINCT link FROM noticia WHERE periodico='elespectador'"
cur = conexion.cursor()
cur.execute(query)
noticias = cur.fetchall()
noticias = [n[0] for n in noticias]
for noticia in noticias:
    elespectador.imagenes(noticia)
    time.sleep(10)

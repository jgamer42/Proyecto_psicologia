import configparser
import os
from dotenv import load_dotenv
import mysql.connector as sql
load_dotenv()

rootPath= os.getenv("PROJECT_PATH")
config = configparser.ConfigParser()
config.sections()
config.read(f"{rootPath}/general.cfg")
puntos = list(dict(config["palabras_clave"]).keys())
conexion = sql.connect(
    host="localhost",
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWD"),
    database=os.getenv("DB_NAME"),
)

for punto in puntos:
    cur = conexion.cursor()
    query = f"INSERT INTO punto (Nombre) VALUES ('{punto}')"
    cur.execute(query)
conexion.commit()
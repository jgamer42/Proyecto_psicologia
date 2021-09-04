import configparser
import os
from dotenv import load_dotenv
import mysql.connector as sql
load_dotenv()

rootPath= os.getenv("PROJECT_PATH")
config = configparser.ConfigParser()
config.sections()
config.read(f"{rootPath}/general.cfg")
actores = list(dict(config["agrupador"]).keys())
partidos = dict(config["partidos"])
conexion = sql.connect(
    host="localhost",
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWD"),
    database=os.getenv("DB_NAME"),
)

for actor in actores:
    for partido in partidos.keys():
        if actor in partidos[partido]:
            cur = conexion.cursor()
            query = f"SELECT id FROM grupo WHERE nombre='{partido}'"
            cur.execute(query)
            llaveForanea = cur.fetchall()[0][0]
            query = f"INSERT INTO actor (Nombre,grupo) VALUES ('{actor}',{llaveForanea})"
            cur.execute(query)
            conexion.commit()
            cur.close()
            break

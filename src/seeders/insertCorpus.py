import os
from dotenv import load_dotenv
import mysql.connector as sql
import json
load_dotenv()
conexion = sql.connect(
    host="localhost",
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWD"),
    database=os.getenv("DB_NAME"),
)
base_path = os.getenv("PROJECT_PATH")
corpus_path = f"{base_path}/src/corpus"

def insertar_noticias(data):
    cur = conexion.cursor()
    try:
        query_noticia = f"INSERT INTO noticia (titulo,contenido,periodico,fecha,link) VALUES ('{data['titulo']}','{data['contenido']}','{medio}','{data['fecha']}','{data['Link']}')"
    except:
        query_noticia = f"INSERT INTO noticia (titulo,contenido,periodico,fecha,link) VALUES ('{data['titulo']}','{data['contenido']}','{medio}','{data['fecha']}','{data['link']}')"
    cur.execute(query_noticia)
    conexion.commit()
    cur.execute("SELECT MAX(ID) FROM noticia")
    id_noticia = cur.fetchone()
    id_noticia = id_noticia[0]
    return id_noticia

def insertar_punto_noticia(punto,id_noticia):
    cur = conexion.cursor()
    cur.execute(f"SELECT ID FROM punto WHERE nombre='{punto}'")
    id_punto = cur.fetchone()
    id_punto = id_punto[0]
    query_punto_noticia = f"INSERT INTO punto_noticia (noticia,punto) VALUES ({id_noticia},{id_punto})"
    cur.execute(query_punto_noticia)
    conexion.commit()

def insertar_actor_noticia(actor,id_noticia):
    cur = conexion.cursor()
    try:
        aux=actor.replace(" ","_")
    except:
        aux=actor
    try:
        cur.execute(f"SELECT ID FROM actor WHERE nombre='{aux}'")
        id_actor = cur.fetchone()
        id_actor = id_actor[0]
        query_actor_noticia = f"INSERT INTO actor_noticia (noticia,actor) VALUES ({id_noticia},{id_actor})"
        cur.execute(query_actor_noticia)
        conexion.commit()
    except:
        print(data["titulo"])


medios = os.listdir(corpus_path)
for medio in medios:
    archivos = os.listdir(f"{corpus_path}/{medio}/json")
    for archivo in archivos:
        
        jsonCargado = open(f"{corpus_path}/{medio}/json/{archivo}")
        data = json.load(jsonCargado)
        data["contenido"] = data["contenido"].replace("'"," ")
        noticia = insertar_noticias(data)
        if len(data["puntos"])== 0:
            print(f"{noticia} no tiene puntos")
        else:
            for punto in data["puntos"]:
                insertar_punto_noticia(punto,noticia)

        if len(data["actores"])== 0:
            print(f"{noticia} no tiene actores")
        else:
            for actor in data["actores"]:
                insertar_actor_noticia(actor,noticia)
        
        
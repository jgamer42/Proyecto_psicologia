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
medios = os.listdir(corpus_path)
for medio in medios:
    archivos = os.listdir(f"{corpus_path}/{medio}/json")
    for archivo in archivos:
        cur = conexion.cursor()
        jsonCargado = open(f"{corpus_path}/{medio}/json/{archivo}")
        data = json.load(jsonCargado)
        data["contenido"] = data["contenido"].replace("'"," ")
        try:
            query_noticia = f"INSERT INTO noticia (titulo,contenido,periodico,fecha,link) VALUES ('{data['titulo']}','{data['contenido']}','{medio}','{data['fecha']}','{data['Link']}')"
        except:
            query_noticia = f"INSERT INTO noticia (titulo,contenido,periodico,fecha,link) VALUES ('{data['titulo']}','{data['contenido']}','{medio}','{data['fecha']}','{data['link']}')"
        cur.execute(query_noticia)
        conexion.commit()
        
        cur.execute("SELECT MAX(ID) FROM noticia")
        id_noticia = cur.fetchone()
        id_noticia = id_noticia[0]
        for punto in data["puntos"]:
            cur.execute(f"SELECT ID FROM punto WHERE nombre='{punto}'")
            id_punto = cur.fetchone()
            id_punto = id_punto[0]
            query_punto_noticia = f"INSERT INTO punto_notica (noticia,punto) VALUES ({id_noticia},{id_punto})"
            cur.execute(query_punto_noticia)
            conexion.commit()
        
        for actor in data["actores"]:
            try:
                aux=actor.replace(" ","_")
            except:
                aux=actor
            try:
                print(f"SELECT ID FROM actor WHERE nombre='{aux}'")
                cur.execute(f"SELECT ID FROM actor WHERE nombre='{aux}'")
                id_actor = cur.fetchone()
                id_actor = id_actor[0]
                query_actor_noticia = f"INSERT INTO actor_notica (noticia,actor) VALUES ({id_noticia},{id_actor})"
                cur.execute(query_actor_noticia)
                conexion.commit()
            except:
                print(data["titulo"])
        
        
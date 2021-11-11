import configparser
import os
from dotenv import load_dotenv
import mysql.connector as sql
import escritor
load_dotenv()

rootPath= os.getenv("PROJECT_PATH")
config = configparser.ConfigParser()
config.sections()
config.read(f"{rootPath}/general.cfg")
conexion = sql.connect(
    host="localhost",
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWD"),
    database=os.getenv("DB_NAME"),
)

def fechas_unicas():
    cur = conexion.cursor()
    sql = "SELECT fecha FROM noticia"
    cur.execute(sql)
    a = cur.fetchall()
    fechas = list(set([c[0] for c in a ]))
    años = list(set([año.split("/")[-1] for año in fechas]))
    años = [año for año in años if año not in ["2020","2021","2021,","2020,"]]
    años.sort()
    return años


def total_noticias():
    sql = f"SELECT * FROM noticia"
    noticias = ejecutarSql(sql)
    return len(noticias)

def difusorMeses(numeroMes):
    meses=["Nodefinido","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    return meses[numeroMes]

def ejecutarSql(sql):
    cur = conexion.cursor()
    cur.execute(sql)
    noticias = cur.fetchall()
    return noticias

def getData(accion):
    if accion == "punto":
        data = config["palabras_clave"].keys()
    elif accion == "actor":
        data = config["agrupador"].keys()
    return data 

def totales(accion):
    salida = {}
    data = getData(accion)
    for d in data:
        sql = f"SELECT noticia.link FROM {accion}_noticia,noticia INNER JOIN {accion} WHERE {accion}.nombre='{d}' AND {accion}_noticia.{accion}={accion}.id AND noticia.id={accion}_noticia.noticia AND noticia.fecha LIKE '%201%'"
        noticias = ejecutarSql(sql)
        noticias = list(set([noticia[0] for noticia in noticias]))
        if len(noticias) != 0:  
            salida[d] = len(noticias)
    return salida

def porFechas(accion,periodico):
    salida = {}
    años = fechas_unicas()
    data = getData(accion)
    for d in data:
        for año in años:
            sql = f'''SELECT noticia.titulo,noticia.fecha
            FROM noticia INNER JOIN {accion}_noticia, {accion} WHERE 
            {accion}.nombre='{d}' AND 
            {accion}_noticia.{accion}={accion}.id AND 
            noticia.fecha LIKE '%{año}' AND 
            noticia.id={accion}_noticia.noticia AND
            noticia.periodico='{periodico}'
            '''
            noticias = ejecutarSql(sql)
            if len(noticias) != 0:
                try:
                    salida[d].keys()
                except:
                    salida[d] = {}
                try:
                    salida[d][año].keys()
                except:
                    salida[d][año] = {}
                for noticia in noticias:
                    mes = int(noticia[1].split("/")[1])
                    mes = difusorMeses(mes)
                    try:
                        salida[d][año][mes].append(noticia[0])
                    except:
                        #salida[d][año][mes] = 1
                        salida[d][año][mes] =[noticia[0]]
    return salida



def totalGrupos():
    salida = {}
    partidos = config["partidos"]
    for partido in partidos:
        sql = f'''SELECT DISTINCT noticia.link FROM noticia INNER JOIN actor,grupo,actor_noticia
        WHERE 
        actor.grupo=grupo.id AND
        grupo.nombre='{partido}' AND
        actor_noticia.actor=actor.id AND
        actor_noticia.noticia=noticia.id AND
        noticia.fecha LIKE '%201%'
        '''
        data = ejecutarSql(sql)
        if len(data) != 0:
            aux = [d[0] for d in data]
            salida[partido] = len(aux)
            #print(partido,len(salida[partido]))

    return salida

def grupoFecha(periodico):
    salida = {}
    partidos = config["partidos"]
    años = fechas_unicas()
    for partido in partidos:
        for año in años:
            sql = f'''SELECT DISTINCT noticia.titulo,noticia.fecha FROM noticia INNER JOIN actor,grupo,actor_noticia
            WHERE 
            actor.grupo=grupo.id AND
            grupo.nombre='{partido}' AND
            actor_noticia.actor=actor.id AND
            actor_noticia.noticia=noticia.id AND
            noticia.fecha LIKE '%{año}' AND
            noticia.periodico='{periodico}'
            '''
            data = ejecutarSql(sql)
            if len(data) != 0:
                try:
                    salida[partido].keys()
                except:
                    salida[partido] = {}
                try:
                    salida[partido][año].keys()
                except:
                    salida[partido][año] = {}
                for noticia in data:
                    mes = int(noticia[1].split("/")[1])
                    mes = difusorMeses(mes)
                    try:
                        #salida[partido][año][mes] += 1
                        salida[partido][año][mes].append(noticia[0])
                    except:
                        #salida[partido][año][mes] = 1
                        salida[partido][año][mes] = [noticia[0]]
                        

    return salida

def grupoPunto(periodico):
    puntos = getData("punto")
    salida = {}
    partidos = config["partidos"]
    for partido in partidos:
        for punto in puntos:
            sql = f'''SELECT DISTINCT titulo FROM noticia INNER JOIN punto,actor,actor_noticia,punto_noticia,grupo
            WHERE 
            noticia.id = punto_noticia.noticia AND
            noticia.id = actor_noticia.noticia AND
            actor.id = actor_noticia.actor AND 
            punto.id = punto_noticia.punto AND
            grupo.id = actor.grupo AND
            grupo.nombre='{partido}' AND
            punto.nombre='{punto}' AND
            noticia.fecha LIKE '%201%' AND
            noticia.periodico='{periodico}'
            '''
            noticias = ejecutarSql(sql)
            if len(noticias) != 0:
                try:
                    salida[partido].keys()
                except:
                    salida[partido] = {}
                    
                salida[partido][punto] = len(noticias)
    return salida

def totalesPartido():
    salida = {}
    partidos = config["partidos"]
    periodicos = ["eltiempo","elespectador"]
    for periodico in periodicos:
        for partido in partidos:
            sql = f'''SELECT DISTINCT link FROM noticia INNER JOIN actor,grupo,actor_noticia
            WHERE 
            noticia.id = actor_noticia.noticia AND
            actor.id = actor_noticia.actor AND
            noticia.fecha LIKE "%201%" AND
            grupo.nombre = "{partido}" AND
            noticia.periodico = '{periodico}' AND
            grupo.id = actor.grupo
            '''
            noticias = ejecutarSql(sql)
            if len(noticias) != 0:
                try:
                    salida[periodico].keys()
                except:
                    salida[periodico] = {}     
                salida[periodico][partido] = len(noticias)
    return salida

def totalesPunto():
    salida = {}
    puntos = getData("punto")
    periodicos = ["eltiempo","elespectador"]
    for periodico in periodicos:
        for punto in puntos:
            sql = f'''SELECT DISTINCT link FROM noticia INNER JOIN punto,punto_noticia
            WHERE 
            noticia.id = punto_noticia.noticia AND
            punto.id = punto_noticia.punto AND
            noticia.fecha LIKE "%201%" AND
            punto.nombre = "{punto}" AND
            noticia.periodico = '{periodico}'
            '''
            noticias = ejecutarSql(sql)
            if len(noticias) != 0:
                try:
                    salida[periodico].keys()
                except:
                    salida[periodico] = {}     
                salida[periodico][punto] = len(noticias)
    return salida
    

def totalesAño():
    salida = {}
    años = fechas_unicas()
    periodicos = ["eltiempo","elespectador"]
    for periodico in periodicos:
        for año in años:
            sql = f'''SELECT DISTINCT link FROM noticia
            WHERE 
            noticia.fecha LIKE "%{año}%" AND
            noticia.periodico = '{periodico}'
            '''
            noticias = ejecutarSql(sql)
            if len(noticias) != 0:
                try:
                    salida[periodico].keys()
                except:
                    salida[periodico] = {}     
                salida[periodico][año] = len(noticias)
    return salida
#escritor.csvFechas(grupoPunto())
#escritor.csvAños(grupoFecha())
#print(grupoFecha("eltiempo"))
#print(grupoPunto("eltiempo"))
#escritor.csvAños(porFechas("punto"))
#print(totales("punto"))
#print(totalesPartido("elespectador"))
#escritor.csvFechas(totalesPartido())
#escritor.csvFechas(totalesPunto())
escritor.csvFechas(totalesAño())
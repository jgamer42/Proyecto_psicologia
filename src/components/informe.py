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
    años = [año for año in años if año not in ["2020","2021","2021,"]]
    años.sort()
    return años

def medioNoticia():
    salida = {}
    medios = ["eltiempo","elespectador"]
    for medio in medios:
        sql = f"SELECT link FROM noticia WHERE periodico='{medio}' AND fecha LIKE '%201%'"
        noticias = ejecutarSql(sql)
        noticias = list(set([noticia[0] for noticia in noticias]))
        salida[medio] = len(noticias)
    return salida

def fechasNoticia():
    años = fechas_unicas()
    salida={}
    for año in años:
        salida[año] = {}
        sql = f"SELECT link,fecha FROM noticia WHERE fecha LIKE '%{año}'"
        noticias = ejecutarSql(sql)
        for noticia in noticias:
            mes = int(noticia[1].split("/")[1])
            mes = difusorMeses(mes)
            try:
                #salida[año][mes].append(noticia[0])
                salida[año][mes] += 1
            except:
                salida[año][mes] = 1
                #salida[año][mes].append(noticia[0])
    return salida

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

def porFechas(accion):
    salida = {}
    años = fechas_unicas()
    data = getData(accion)
    for d in data:
        for año in años:
            sql = f"SELECT noticia.link,noticia.fecha FROM noticia INNER JOIN {accion}_noticia, {accion} WHERE {accion}.nombre='{d}' AND {accion}_noticia.{accion}={accion}.id AND noticia.fecha LIKE '%{año}' AND noticia.id={accion}_noticia.noticia"
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
                        salida[d][año][mes] += 1
                    except:
                        salida[d][año][mes] = 1
                        #salida[d][año][mes].append(noticia[0])
    return salida

def porMedio(accion):
    salida = {}
    medios = ["eltiempo","elespectador"]
    data = getData(accion)
    for d in data:
        for medio in medios:
            sql = f"SELECT noticia.link FROM {accion}_noticia,noticia INNER JOIN {accion} WHERE {accion}.nombre='{d}' AND {accion}_noticia.{accion}={accion}.id AND noticia.periodico='{medio}' AND noticia.id={accion}_noticia.noticia AND noticia.fecha LIKE '%201%'"
            noticias = ejecutarSql(sql)
            noticias = list(set([noticia[0] for noticia in noticias]))
            if len(noticias) != 0:
                try:  
                    salida[d].keys()
                except:
                    salida[d] = {}
                salida[d][medio] = len(noticias)
    return salida

def informeCompleto():
    salida = {}
    partidos = config["partidos"]
    actores = config["agrupador"].keys()
    puntos = config["palabras_clave"].keys()
    medios = ["eltiempo","elespectador"]
    fechas = fechas_unicas()
    for medio in medios:
        for partido in partidos.keys():
            for actor in actores:
                for punto in puntos:
                    for fecha in fechas:
                        if actor in partidos[partido]:
                            query = f'''SELECT link,fecha FROM noticia INNER JOIN actor,actor_noticia,punto_noticia,punto,grupo WHERE
                            noticia.fecha LIKE '%{fecha}' AND
                            noticia.periodico = '{medio}' AND
                            noticia.id=actor_noticia.noticia AND 
                            noticia.id=punto_noticia.noticia AND
                            punto_noticia.punto = punto.id AND
                            punto.nombre='{punto}' AND
                            actor.nombre='{actor}' AND
                            actor.id=actor_noticia.actor AND
                            actor.grupo=grupo.id AND
                            grupo.nombre='{partido}'
                            '''
                            noticias = ejecutarSql(query)
                            if len(noticias) != 0:
                                try:
                                    salida[partido].keys()
                                except:
                                    salida[partido] = {}
                                try:
                                    salida[partido][medio].keys()
                                except:
                                    salida[partido][medio] = {}
                                try:
                                    salida[partido][medio][punto].keys()
                                except:
                                    salida[partido][medio][punto] = {}
                                try:
                                    salida[partido][medio][punto][fecha].keys()
                                except:
                                    salida[partido][medio][punto][fecha] = {}
                                for noticia in noticias:
                                    mes = int(noticia[1].split("/")[1])
                                    mes = difusorMeses(mes)
                                    try:
                                        salida[partido][medio][punto][fecha][mes].append(noticia[0])
                                    except:
                                        salida[partido][medio][punto][fecha][mes] = []
                                        salida[partido][medio][punto][fecha][mes].append(noticia[0])
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


def datosPowerBi():
    salida = []
    query = f'''SELECT DISTINCT noticia.titulo,noticia.fecha,grupo.nombre,punto.nombre,actor.nombre,noticia.periodico 
    FROM noticia INNER JOIN grupo,punto_noticia,actor_noticia,punto,actor 
    WHERE 
    noticia.id=actor_noticia.noticia AND 
    noticia.id=punto_noticia.noticia AND
    punto.id=punto_noticia.punto AND 
    actor.id=actor_noticia.actor AND
    grupo.id=actor.grupo AND noticia.fecha LIKE '%201%'
    '''
    datos = ejecutarSql(query)
    for dato in datos:
        fecha = dato[1]
        mes = int(fecha.split("/")[1])
        mes = difusorMeses(mes)
        if "2021," in fecha:
            fechaCorregida = fecha.replace("2021,","2021")
        else:
            fechaCorregida = fecha
        año = fechaCorregida.split("/")[-1]
        aux = list(dato[0:1])+[fechaCorregida]+list(dato[2:]) +[año,mes]
        aux = tuple(aux)
        if año not in ["2019","2020","2021"]:
            salida.append(aux)
    return salida

def grupoFecha():
    salida = {}
    partidos = config["partidos"]
    años = fechas_unicas()
    for partido in partidos:
        for año in años:
            sql = f'''SELECT DISTINCT noticia.link,noticia.fecha FROM noticia INNER JOIN actor,grupo,actor_noticia
            WHERE 
            actor.grupo=grupo.id AND
            grupo.nombre='{partido}' AND
            actor_noticia.actor=actor.id AND
            actor_noticia.noticia=noticia.id AND
            noticia.fecha LIKE '%{año}'
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
                        salida[partido][año][mes] += 1
                    except:
                        salida[partido][año][mes] = 1

    return salida

def grupoPunto():
    puntos = getData("punto")
    salida = {}
    partidos = config["partidos"]
    for partido in partidos:
        for punto in puntos:
            sql = f'''SELECT DISTINCT link FROM noticia INNER JOIN punto,actor,actor_noticia,punto_noticia,grupo
            WHERE 
            noticia.id = punto_noticia.noticia AND
            noticia.id = actor_noticia.noticia AND
            actor.id = actor_noticia.actor AND 
            punto.id = punto_noticia.punto AND
            grupo.id = actor.grupo AND
            grupo.nombre='{partido}' AND
            punto.nombre='{punto}' AND
            noticia.fecha LIKE '%201%'
            '''
            noticias = ejecutarSql(sql)
            if len(noticias) != 0:
                try:
                    salida[partido].keys()
                except:
                    salida[partido] = {}
                salida[partido][punto] = len(noticias)
    return salida

#print(grupoFecha())
#data["totalMedio"] = medioNoticia()
#data["totalFechas"] = fechasNoticia()
#data["totalGrupos"] = totalGrupos()
#data["totalPuntos"] = totales("punto")
#data["puntosPorFecha"] = porFechas("punto")
#data["puntosPorMedio"] = porMedio("punto")
#data["informeFinal"] = informeCompleto()
#print(fechasNoticia())
#a = porFechas("punto")
#print(grupoPunto())
escritor.csvFechas(grupoPunto())
#escritor.jsonInforme(data)

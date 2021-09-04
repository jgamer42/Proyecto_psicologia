import requests
import os
import json
from slugify import slugify
from lxml import html
from dotenv import load_dotenv
import time
import random
load_dotenv() 
import site
site.addsitedir(os.getenv("PROJECT_PATH")+"/src")
from components import fechas
from components.bussines import puntosAcuerdo,personajes2
def procesar(link):
    base = os.getenv("PROJECT_PATH")
    data = requests.get(link)
    data = data.text
    loaded_html = html.fromstring(data)
    titulo = loaded_html.xpath("//h1[@itemprop]/text()")
    fecha = loaded_html.xpath('//div[@class="img_info h-seccion"]/div[@class="author_data"]/span[@class="publishedAt"]/text()')
    contenido = loaded_html.xpath('//div/p[@class="contenido"]/text()')
    contenido_auxiliar = loaded_html.xpath('//span[@class="articulo-subtitulo"]/text()')
    archivo = open(base+"/src/model.json")
    salida = json.load(archivo)
    salida["titulo"] = slugify(titulo[0])
    salida["fecha"] = fechas.normalizar(fecha[0])
    salida["contenido"] = " ".join(contenido)
    salida["aux"] = " ".join(contenido_auxiliar)
    salida["medio"] = "eltiempo"
    salida["link"] = link
    salida["puntos"] = puntosAcuerdo.etiquetar(salida["contenido"])
    salida["actores"] = personajes2.etiquetar(salida["contenido"])
    return salida

def filtro_Autor(links):
    salida = []
    for link in links:
        try:
            data = requests.get(link)
            data = data.text
            loaded_html = html.fromstring(data)
            autor = loaded_html.xpath('//span[@class="nombre who"]/text()')
            if "POLÍTICA" in autor:
                salida.append(link)
            time.sleep(random.choice([60,120,180]))
            print("esperando")
        except:
            print("aglo salio mal")
            continue
    return salida

def filtrar(link):
    data = requests.get(link)
    data = data.text
    loaded_html = html.fromstring(data)
    try:
        autor = loaded_html.xpath('//span[@class="nombre who"]/text()')
        if "POLÍTICA" in autor:
            return link
    except:
        print(f"fallo {link}")
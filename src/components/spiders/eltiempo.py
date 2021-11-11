
import unidecode
import requests
import os
import json
from slugify import slugify
from lxml import html
from dotenv import load_dotenv
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
    autor = loaded_html.xpath('//span[@class="nombre who"]/text() |//span[@class="who"]/text()')
    archivo = open(base+"/src/model.json")
    salida = json.load(archivo)
    salida["titulo"] = slugify(titulo[0])
    salida["fecha"] = fechas.normalizar(fecha[0])
    salida["contenido"] = unidecode.unidecode(str(" ".join(contenido)).lower().strip())
    salida["aux"] = unidecode.unidecode(str(" ".join(contenido_auxiliar)).lower().strip())
    salida["medio"] = "eltiempo"
    salida["link"] = link
    salida["autor"] = autor[0]
    salida["puntos"] = puntosAcuerdo.etiquetar(salida["contenido"])
    salida["actores"] = personajes2.etiquetar(salida["contenido"])
    return salida

def filtrar(link):
    data = requests.get(link)
    data = data.text
    loaded_html = html.fromstring(data)
    try:
        autor = loaded_html.xpath('//span[@class="nombre who"]/text() |//span[@class="who"]/text()')
        if "POLÍTICA" in autor or "politica" in autor or 'Política' in autor or 'Redacción EL TIEMPO' in autor or 'Redacción EL TIEMPO' in autor or 'Política y ELTIEMPO.COM' in autor or 'POLÍTICA\xa0' in autor or 'ELTIEMPO.COM' in autor or 'Redacción Política' in autor or 'REDACCIÓN EL TIEMPO' in autor:
            return link
        else:
            print(f"no paso el filtro {link} {autor}")
    except:
        print(f"fallo {link}")


def bajar(link):
    data = requests.get(link)
    data = data.text
    a = open("salida.html","w+")
    a.write(data)

#print(filtrar("https://www.eltiempo.com/politica/proceso-de-paz/como-avanza-el-proceso-de-paz-en-colombia-2020-segun-la-onu-517866"))
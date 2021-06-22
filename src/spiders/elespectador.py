import requests
import os
import json
from slugify import slugify
from lxml import html
from dotenv import load_dotenv
load_dotenv() 
import site
site.addsitedir(os.getenv("PROJECT_PATH")+"/src")
import escritor

def procesar(link):
    base = os.getenv("PROJECT_PATH")
    data = requests.get(link)
    data = data.text
    loaded_html = html.fromstring(data)
    titulo = loaded_html.xpath("//div/h1/text()")
    fecha = loaded_html.xpath('//div[@class="ArticleHeader"]/div/text()')
    encabezado = loaded_html.xpath('//div[@class="ArticleHeader"]/div/div/text()')
    contenido = loaded_html.xpath('//p/text()')
    contenido_auxiliar = loaded_html.xpath("//p/i/text() | //p/i/b/text() | //p/a/text() ")
    archivo = open(base+"/src/model.json")
    salida = json.load(archivo)
    salida["titulo"] = slugify(titulo[0])
    salida["fecha"] = fecha[0]
    salida["contenido"] = encabezado[0] + " ".join(contenido)
    salida["aux"] = " ".join(contenido_auxiliar)
    salida["medio"] = "elespectador"
    salida["link"] = link
    return salida

def filtro_Autor(links):
    salida = []
    for link in links:
        data = requests.get(link)
        data = data.text
        loaded_html = html.fromstring(data)
        autor = loaded_html.xpath('//h3[@class="ACredit-Author"]/a/text() | //h3[@class="ACredit-Author"]/text()')[0]
        if "Política" in autor:
            salida.append(link)
    return salida


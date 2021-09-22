import requests
import os
import json
import time
import random
from slugify import slugify
from lxml import html,etree
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
    titulo = loaded_html.xpath("//div/h1/text()")
    fecha = loaded_html.xpath('//div[@class="ArticleHeader"]/div/text()')
    encabezado = loaded_html.xpath('//div[@class="ArticleHeader"]/div/div/text()')
    contenido = loaded_html.xpath('//p/text()')
    contenido_auxiliar = loaded_html.xpath("//p/i/text() | //p/i/b/text() | //p/a/text() ")
    autor = loaded_html.xpath('//h3[@class="ACredit-Author"]/a/text() | //h3[@class="ACredit-Author"]/text()')[0]
    archivo = open(base+"/src/model.json")
    salida = json.load(archivo)
    salida["titulo"] = slugify(titulo[0])
    salida["fecha"] = fechas.normalizar(fecha[0])
    salida["contenido"] = encabezado[0] + " ".join(contenido)
    salida["aux"] = " ".join(contenido_auxiliar)
    salida["medio"] = "elespectador"
    salida["link"] = link
    salida["autor"] = autor
    salida["puntos"] = puntosAcuerdo.etiquetar(salida["contenido"])
    salida["actores"] = personajes2.etiquetar(salida["contenido"])
    return salida

def filtrar(link):
    data = requests.get(link)
    data = data.text
    loaded_html = html.fromstring(data)
    try:
        autor = loaded_html.xpath('//h3[@class="ACredit-Author"]/a/text() | //h3[@class="ACredit-Author"]/text()')[0].strip()
        if "Política" in autor or "-Redacción Politíca" in autor or 'Redacción Política' in autor or autor in "Redacción Politíca":
            return link
        else:
            print(f"no paso el filtro {link} {autor}")
    except:
        print(f"falo {link}")

def imagenes(link):
    data = requests.get(link)
    data = data.text
    loaded_html = html.fromstring(data)
    regex="//script[@type='application/ld+json']"
    prueba = loaded_html.xpath(regex)
    for p in prueba:
        rawjs = etree.tostring(p)
        rawjs = rawjs.decode()
        step1 = rawjs.replace('<script type="application/ld+json">',"")
        step2 = step1.replace("</script>","")
        step3 = step2.replace("@","")
        clean = json.loads(step3)
        try:
            img = clean["url"]
            if "jpg" in img:
                print(img)
                os.system(f"wget '{img}'")          
        except:
            pass
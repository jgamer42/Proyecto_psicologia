import configparser
import os
from dotenv import load_dotenv
import unicodedata
from copy import deepcopy
load_dotenv() 

def etiquetar(texto):
    textoNormalizado=texto.lower()
    textoNormalizado = remove_accents(textoNormalizado)
    salida = []
    rootPath= os.getenv("PROJECT_PATH")
    config = configparser.ConfigParser()
    config.sections()
    config.read(f"{rootPath}/general.cfg")
    actores = config["actores"]["actores"].lower()
    actores = list(set(actores.split(",")))
    for actor in actores:
        if actor in textoNormalizado:
            salida.append(actor)
    salida = limpiarPersonajes(salida)
    salida = normalizarPersonajes(salida)
    return list(set(salida))

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    text = list(str(only_ascii))[1:]
    text = "".join(text)
    text = text.replace("'","")
    return text

def limpiarPersonajes(listaPersonajes):
    salida = deepcopy(listaPersonajes)
    print(salida,listaPersonajes)
    if "vicepresidenta" in listaPersonajes and "martha lucia" in listaPersonajes:
        salida.remove("martha lucia")
        #pass
    elif (("duque" in listaPersonajes or "ivan duque" in listaPersonajes) and ("presidente" in listaPersonajes)):
        salida.remove("presidente")
        salida.remove("duque")
        #pass
    elif "uribe" in listaPersonajes and "alvaro uribe" in listaPersonajes:
       salida.remove("uribe")
       #pass
    elif "alcaldesa de bogota" in listaPersonajes and "claudia lopez":
        salida.remove("alcaldesa de bogota")
    return salida

def normalizarPersonajes(listaPersonajes):
    salida = deepcopy(listaPersonajes)
    if "vicepresidenta" in listaPersonajes:
        salida.append("martha lucia")
        salida.remove("vicepresidenta")
    elif "alcaldesa de bogota" in listaPersonajes:
        salida.append("claudia lopez")
        salida.remove("alcaldesa de bogota")
    elif "uribe" in listaPersonajes:
        salida.append("alvaro uribe")
        salida.remove("uribe")
    elif "duque" in listaPersonajes or "presidente" in listaPersonajes:
        salida.append("ivan duque")
        try:
            salida.remove("duque")
        except:
            pass
        try:
            salida.remove("presidente")
        except:
            pass
    return salida
import configparser
import os
from dotenv import load_dotenv
load_dotenv() 

def etiquetar(texto):
    salida = []
    rootPath= os.getenv("PROJECT_PATH")
    config = configparser.ConfigParser()
    config.sections()
    config.read(f"{rootPath}/general.cfg")
    puntos = config["palabras_clave"]
    for punto in puntos:
        palabrasClave = list(set(puntos[punto].lower().split(",")))
        for palabra in palabrasClave:
            if palabra in texto:
                if punto in salida:
                    pass
                else:
                    salida.append(punto)
    return salida
etiquetar("hola")
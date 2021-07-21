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
    actores = config["actores"]["actores"]
    actores = list(set(actores.split(",")))
    for actor in actores:
        for palabra in texto:
            if actor == palabra:
                salida.append(actor)
                break
    return salida

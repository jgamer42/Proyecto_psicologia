import configparser
import os
from dotenv import load_dotenv
load_dotenv()

def etiquetar(actores):
    salida = []
    rootPath= os.getenv("PROJECT_PATH")
    config = configparser.ConfigParser()
    config.sections()
    config.read(f"{rootPath}/general.cfg")
    grupos=dict(config["partidos"])
    for actor in actores:
        for grupo in grupos.keys():
            if actor in grupos[grupo]:
                salida.append(grupo)
    return salida
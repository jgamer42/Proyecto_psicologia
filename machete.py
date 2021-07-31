import os
import json
from dotenv import load_dotenv
load_dotenv() 
from src.components.bussines import personajes
def marcarPersonajes():
    base = os.getenv("PROJECT_PATH")+"/src/corpus"
    carpetas = os.listdir(base)
    for carpeta in carpetas:
        ruta = f"{base}/{carpeta}/json"
        archivos = os.listdir(ruta)
        for archivo in archivos:
            print(f"{ruta}/{archivo}")
            jsonCargado = open(f"{ruta}/{archivo}")
            data = json.load(jsonCargado)
            texto = data["aux"]+data["contenido"]
            actores = personajes.etiquetar(texto)
            data["actores"] = actores
            jsonEscritor = open(f"{ruta}/{archivo}","a")
            json.dump(data,jsonEscritor)
marcarPersonajes()
import os
import json
from dotenv import load_dotenv
load_dotenv() 
from src.components.bussines import personajes2
def marcarPersonajes():
    base = os.getenv("PROJECT_PATH")+"/src/corpus"
    carpetas = os.listdir(base)
    for carpeta in carpetas:
        ruta = f"{base}/{carpeta}/json"
        archivos = os.listdir(ruta)
        for archivo in archivos:
            try:
                print(f"{ruta}/{archivo}")
                jsonCargado = open(f"{ruta}/{archivo}")
                data = json.load(jsonCargado)
                texto = data["aux"]+data["contenido"]
                actores = personajes2.etiquetar(texto)
                data["actores"] = list(set(actores))
                jsonEscritor = open(f"{ruta}/{archivo}","w")
                json.dump(data,jsonEscritor)
                print(actores)
            except:
                print(f"fallo {ruta}/{archivo}")
marcarPersonajes()
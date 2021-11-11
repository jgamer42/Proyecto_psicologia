import os 
import configparser
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = configparser.ConfigParser()
config.sections()
config.read(f"{path}/general.cfg")
palabras=dict(config["palabras_clave"])["punto1"]
palabras = set(palabras.lower().split(","))

ruta = f"{path}/src/corpusOrganizado/eltiempo/punto/punto1/2016/Septiembre"
notas = os.listdir(ruta)
for nota in notas:
    print(nota)
    archivo = open(f"{ruta}/{nota}","r")
    data = set(archivo.read().lower().split(" "))
    data = [d for d in data if d not in ["[","]",",",":","."] and "http" not in d]
    #print(archivo.read())
    for d in data:
        if d in palabras:
            print(d)
print([p for p in palabras if len(p.split(" ")) >= 2])
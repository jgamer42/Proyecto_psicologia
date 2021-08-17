import configparser
import os
from dotenv import load_dotenv
import unicodedata
from copy import deepcopy
load_dotenv()

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    text = list(str(only_ascii))[1:]
    text = "".join(text)
    text = text.replace("'","")
    return text

def etiquetar(texto):
    salida = []
    rootPath= os.getenv("PROJECT_PATH")
    config = configparser.ConfigParser()
    config.sections()
    config.read(f"{rootPath}/general.cfg")
    personajes=dict(config["agrupador"])
    texto_normalizado=texto.lower()
    texto_normalizado=remove_accents(texto_normalizado)
    texto_normalizado=texto_normalizado.strip()
    for palabra in texto:
        for personaje in personajes:
            personajes_normalizados = normalizar_personajes(personajes[personaje])
            if palabra in personajes_normalizados:
                salida.append(personaje)
    return salida

def normalizar_personajes(personajes):
    personajes_normalizados=personajes.split(",")
    personajes_normalizados=[personaje.lower() for personaje in personajes_normalizados]
    personajes_normalizados=list(map(remove_accents,personajes_normalizados))
    return personajes_normalizados

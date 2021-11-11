import os

import inspect
from informe import grupoPunto,grupoFecha,porFechas

def crearCarpetas(periodico,data,raiz):
    global corpusNoOrdenado
    for k in data.keys():
        os.system(f"mkdir '/home/jaime/cosas/codigo/proyecto_psicologia/src/corpusOrganizado/{periodico}/{raiz}/{k}'")
        for año in data[k].keys():
            os.system(f"mkdir '/home/jaime/cosas/codigo/proyecto_psicologia/src/corpusOrganizado/{periodico}/{raiz}/{k}/{año}'")
            for mes in data[k][año].keys():
                os.system(f"mkdir '/home/jaime/cosas/codigo/proyecto_psicologia/src/corpusOrganizado/{periodico}/{raiz}/{k}/{año}/{mes}'")
                aux = inspect.currentframe().f_globals
                notas = aux[f"notas{periodico}"]
                notas = [n.split(".")[0] for n in notas]
                for n in data[k][año][mes]: 
                    if n in notas:
                        os.system(f"cp '{corpusNoOrdenado}/{periodico}/txt/{n}.txt' '/home/jaime/cosas/codigo/proyecto_psicologia/src/corpusOrganizado/{periodico}/{raiz}/{k}/{año}/{mes}/{n}.txt'")

corpusNoOrdenado = "/home/jaime/cosas/codigo/proyecto_psicologia/src/corpus"
#a = grupoPunto("eltiempo")
eltiempoGrupo = grupoFecha("eltiempo")
elespectadorGrupo = grupoFecha("elespectador")
elespectadorPunto = porFechas("punto","elespectador")
eltiempoPunto = porFechas("punto","eltiempo")
#print(eltiempo)
#print(elespectador)

notaselespectador = os.listdir(f"{corpusNoOrdenado}/elespectador/txt")
notaseltiempo = os.listdir(f"{corpusNoOrdenado}/eltiempo/txt")
#print(eltiempoPunto)
crearCarpetas("eltiempo",eltiempoGrupo,"grupo")
crearCarpetas("elespectador",elespectadorGrupo,"grupo")
crearCarpetas("eltiempo",eltiempoPunto,"punto")
crearCarpetas("elespectador",elespectadorPunto,"punto")


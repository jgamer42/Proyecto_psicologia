import os 
import pandas as pd
base_path = "/home/jaime/cosas/codigo/proyecto_psicologia/src/corpusOrganizado"
puntos = ["punto1","punto2","punto3","punto4","punto5"]

data_frames = {}
archivos = os.listdir(base_path)
for medio in archivos:
    if medio not in data_frames.keys():
        data_frames[medio] = {}
    aux = os.listdir(f"{base_path}/{medio}/grupo")
    for grupo in aux:
        if grupo not in data_frames[medio].keys():
            data_frames[medio][grupo] = {}
        aux1 = os.listdir(f"{base_path}/{medio}/grupo/{grupo}")
        for año in aux1:
            if año not in data_frames[medio][grupo].keys():
                data_frames[medio][grupo][año] = {}
            meses_grupo = os.listdir(f"{base_path}/{medio}/grupo/{grupo}/{año}")
            for mes in meses_grupo:
                documentos_grupo_mes = os.listdir(f"{base_path}/{medio}/grupo/{grupo}/{año}/{mes}")
                for punto in puntos:
                    if punto not in data_frames[medio][grupo][año].keys():
                        data_frames[medio][grupo][año][punto] = 0
                    try:
                        documentos_punto_mes = os.listdir(f"{base_path}/{medio}/punto/{punto}/{año}/{mes}")
                    except:
                        continue
                    for d in documentos_punto_mes:
                        if d in documentos_punto_mes:
                            data_frames[medio][grupo][año][punto] += 1

for medio in data_frames.keys():
    for grupo in data_frames[medio].keys():
        nombre=f"salida/{medio}_{grupo}_puntos.csv"
        data = data_frames[medio][grupo]
        a = pd.DataFrame(data)
        a.fillna(0)
        a = a.apply(pd.to_numeric,errors="ignore")
        a.to_csv(nombre)
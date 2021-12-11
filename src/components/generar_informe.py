import os
import pandas as pd
base_path = "/home/jaime/cosas/codigo/proyecto_psicologia/src/corpusOrganizado"
data = {}
general_temporal = {}
general_punto = {}
general_actor = {}
temporal_tiempo = {}
temporal_espectador = {}
temporal_medio = {}
totales_medio = {}
totales_grupo = {}
for medio in os.listdir(base_path):
    #grupo-punto
    #print(medio)
    for elemento in os.listdir(f"{base_path}/{medio}"):
        #gruposEspecificos-puntosEspecificos
        #print("\t",elemento)
        for archivo in os.listdir(f"{base_path}/{medio}/{elemento}"):
            #años
            #print("\t\t",archivo)
            for carpeta in os.listdir(f"{base_path}/{medio}/{elemento}/{archivo}"):
                #print("\t\t\t",carpeta)
                if carpeta not in general_temporal.keys():
                    general_temporal[carpeta] = {}
                if carpeta not in data.keys():
                    data[carpeta] = {}
                for mes in os.listdir(f"{base_path}/{medio}/{elemento}/{archivo}/{carpeta}"):
                    #print("\t\t\t\t",mes)
                    if medio not in temporal_medio.keys():
                        temporal_medio[medio] = {}

                    if carpeta in temporal_medio[medio].keys():
                        temporal_medio[medio][carpeta] += len(os.listdir(f"{base_path}/{medio}/{elemento}/{archivo}/{carpeta}/{mes}"))
                    else:
                        temporal_medio[medio][carpeta] = len(os.listdir(f"{base_path}/{medio}/{elemento}/{archivo}/{carpeta}/{mes}"))

                    if medio == "eltiempo":
                        if carpeta not in temporal_tiempo.keys():
                            temporal_tiempo[carpeta] = {}
                        if mes in temporal_tiempo[carpeta].keys():
                            temporal_tiempo[carpeta][mes] += len(os.listdir(f"{base_path}/{medio}/{elemento}/{archivo}/{carpeta}/{mes}"))
                        else:
                            temporal_tiempo[carpeta][mes] = len(os.listdir(f"{base_path}/{medio}/{elemento}/{archivo}/{carpeta}/{mes}"))
                    else:
                        if carpeta not in temporal_espectador.keys():
                            temporal_espectador[carpeta] = {}
                        if mes in temporal_espectador[carpeta].keys():
                            temporal_espectador[carpeta][mes] += len(os.listdir(f"{base_path}/{medio}/{elemento}/{archivo}/{carpeta}/{mes}"))
                        else:
                            temporal_espectador[carpeta][mes] = len(os.listdir(f"{base_path}/{medio}/{elemento}/{archivo}/{carpeta}/{mes}"))

                    if mes in general_temporal[carpeta].keys():
                        general_temporal[carpeta][mes] += len(os.listdir(f"{base_path}/{medio}/{elemento}/{archivo}/{carpeta}/{mes}"))
                    else:
                        general_temporal[carpeta][mes] = len(os.listdir(f"{base_path}/{medio}/{elemento}/{archivo}/{carpeta}/{mes}"))



                    if mes in data[carpeta].keys():
                        data[carpeta][mes] += len(os.listdir(f"{base_path}/{medio}/{elemento}/{archivo}/{carpeta}/{mes}"))
                    else:
                        data[carpeta][mes] = len(os.listdir(f"{base_path}/{medio}/{elemento}/{archivo}/{carpeta}/{mes}"))


                    if "punto" in archivo:
                        if medio not in general_punto.keys():
                            general_punto[medio] = {}
                        if archivo in general_punto[medio].keys():
                            general_punto[medio][archivo] += len(os.listdir(f"{base_path}/{medio}/{elemento}/{archivo}/{carpeta}/{mes}"))
                        else:
                            general_punto[medio][archivo] = len(os.listdir(f"{base_path}/{medio}/{elemento}/{archivo}/{carpeta}/{mes}"))
                    else:
                        if medio not in general_actor.keys():
                            general_actor[medio]={}
                        if archivo in general_actor.keys():
                            general_actor[medio][archivo] += len(os.listdir(f"{base_path}/{medio}/{elemento}/{archivo}/{carpeta}/{mes}"))
                        else:
                            general_actor[medio][archivo] = len(os.listdir(f"{base_path}/{medio}/{elemento}/{archivo}/{carpeta}/{mes}"))

                    
                    if medio in totales_medio.keys():
                        pass
                    else:
                        totales_medio[medio] = {}

                    if archivo in totales_medio[medio].keys():
                        totales_medio[medio][archivo] += 1
                    else:
                        totales_medio[medio][archivo] = 1
                    
                    if archivo in totales_grupo.keys():
                        pass
                    else:
                        totales_grupo[archivo] = {}

                    if carpeta in totales_grupo[archivo].keys():
                        totales_grupo[archivo][carpeta] += 1
                    else:
                        totales_grupo[archivo][carpeta] = 1

            a = pd.DataFrame(data)
            a = a.fillna(0)
            a = a.apply(pd.to_numeric,errors="ignore")
            a.to_csv(f"salida/{medio}_{archivo}.csv")
            data = {}
#print(general_temporal,"\n",general_punto,"\n",general_actor,"\n",temporal_espectador,"\n\n",temporal_tiempo,"\n\n",temporal_medio)

a = pd.DataFrame(general_temporal)
a = a.fillna(0)
a = a.apply(pd.to_numeric,errors="ignore")
a.to_csv(f"salida/general_temporal.csv")

a = pd.DataFrame(general_punto)
a = a.fillna(0)
a = a.apply(pd.to_numeric,errors="ignore")
a.to_csv(f"salida/general_punto.csv")

a = pd.DataFrame(general_actor)
a = a.fillna(0)
a = a.apply(pd.to_numeric,errors="ignore")
a.to_csv(f"salida/general_actor.csv")

a = pd.DataFrame(temporal_espectador)
a = a.fillna(0)
a = a.apply(pd.to_numeric,errors="ignore")
a.to_csv(f"salida/temporal_espectador.csv")

a = pd.DataFrame(temporal_tiempo)
a = a.fillna(0)
a = a.apply(pd.to_numeric,errors="ignore")
a.to_csv(f"salida/temporal_tiempo.csv")

a = pd.DataFrame(temporal_medio)
a = a.fillna(0)
a = a.apply(pd.to_numeric,errors="ignore")
a.to_csv(f"salida/temporal_medio.csv")

a = pd.DataFrame(totales_medio)
a = a.fillna(0)
a = a.apply(pd.to_numeric,errors="ignore")
a.to_csv(f"salida/totales_medio.csv")


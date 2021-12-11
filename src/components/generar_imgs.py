import os 
import pandas as pd 
import matplotlib.pyplot as plt

data = os.listdir("/home/jaime/cosas/codigo/proyecto_psicologia/src/components/salida")

for archivo in data:
    try:
        data_frame = None
        data_frame = pd.read_csv(f"/home/jaime/cosas/codigo/proyecto_psicologia/src/components/salida/{archivo}")
        nombre = archivo.split(".")[0]
        data_frame.plot(kind="bar",x="Unnamed: 0",figsize=(10,10))
        plt.title(nombre)
        plt.savefig(f"imgs/{nombre}.jpg")
        plt.close()
    except:
        continue

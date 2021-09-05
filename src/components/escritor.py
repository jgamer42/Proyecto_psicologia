import os
from dotenv import load_dotenv
import json
import pandas as pd
from fpdf import FPDF
load_dotenv() 

def txt(modelo):
    base = os.getenv("PROJECT_PATH")
    file = open(base+f"/src/corpus/{modelo['medio']}/txt/{modelo['titulo']}.txt",'w+') 
    file.write(f"titulo: {modelo['titulo']}\n")
    file.write(f"Link: {modelo['link']}\n")
    file.write(f"fecha: {modelo['fecha']}\n")
    file.write(f"contenido: {modelo['contenido']}\n")
    file.write(f"aux: {modelo['aux']}\n")
    file.write(f"actores: {modelo['actores']}\n")
    file.write(f"puntos: {modelo['puntos']}")
    file.close()

def Json(modelo):
    base = os.getenv("PROJECT_PATH")
    file = open(base+f"/src/corpus/{modelo['medio']}/json/{modelo['titulo']}.json",'w+')
    json.dump(modelo,file)

def jsonInforme(data):
    file = open("salida.json",'w+')
    json.dump(data,file)


def csv(data):
    loadData = pd.DataFrame(data,columns=("titulo","fecha","partido","punto","actor","nedio","año","mes"))
    loadData.to_csv("salida.csv",index=False)    

def csvAños(data):
    for d in data.keys():
        try:
            loadData=pd.DataFrame(data[d])
        except:
            loadData=pd.DataFrame(data[d],index=[0])
        loadData = loadData.fillna(0)
        b = {año:"int" for (año,valor) in data[d].items()}
        loadData=loadData.astype(b)
        print(loadData)
        loadData.to_csv(f"{d}.csv")

def csvFechas(data):
    loadData=pd.DataFrame(data)
    loadData = loadData.fillna(0)
    b = {año:"int" for (año,valor) in data.items()}
    loadData=loadData.astype(b)
    print(loadData)
    loadData.to_csv(f"temporal.csv")
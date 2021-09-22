from src.components import google,escritor,googleEltiempo
#import src.components.spiders
import time
from datetime import datetime
import random
import site
site.addsitedir("/home/jaime/cosas/codigo/proyecto_psicologia/src/components/spiders")
inicio = datetime.now()
print("buscando en google")
elespectador = google.buscar("elespectador") 
time.sleep(20)
#eltiempo = google.buscar("eltiempo")
time.sleep(20)
#eltiempoEspecial = googleEltiempo.buscar()
#links = eltiempo+elespectador+eltiempoEspecial
links = elespectador
fin = datetime.now()
print(f"demoro {fin-inicio} y encontro {len(links)}")
inicio = datetime.now()
filtrados = []
print("filtrando")
for link in links:
    periodico = link.split(".")[1]
    spider = __import__(periodico)
    filtrado = spider.filtrar(link)
    if  filtrado != None:
        filtrados.append(link)
        data = spider.procesar(link)
        escritor.txt(data)
        escritor.Json(data)
        esperar = random.randint(10,30)
        #esperar = random.randint(30,420)
        print(f"esperando {esperar}")
        time.sleep(esperar)
    else:
        continue
fin = datetime.now()
print(f"demoro {fin-inicio} y encontro {len(filtrados)}")

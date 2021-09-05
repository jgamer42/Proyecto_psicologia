from src.components import google,escritor
#import src.components.spiders
import time
from datetime import datetime
import random
import site
site.addsitedir("/home/jaime/cosas/codigo/proyecto_psicologia/src/components/spiders")
inicio = datetime.now()
print("buscando en google")
links = google.buscar("elespectador") + google.buscar("eltiempo")
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
        #print(E)
        time.sleep(random.choice([20,30,60,90,120]))
    else:
        print(f"no paso {link}")
        continue
fin = datetime.now()
print(f"demoro {fin-inicio} y encontro {len(filtrados)}")
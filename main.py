from src.components import google,escritor
import src.components.spiders.eltiempo as eltiempo
import src.components.spiders.elespectador as elespectador
import time
import random
print("el tiempo")
print("buscando en google")
links = google.buscar("eltiempo")
print("filtrando")
try:
    filtredLinks = eltiempo.filtro_Autor(links)
except:
    time.sleep(800)
    filtredLinks = eltiempo.filtro_Autor(links)
for link in filtredLinks:
    print(f"procesando:{link}")
    try:
        dato = eltiempo.procesar(link)
        escritor.txt(dato)
        escritor.Json(dato)
        print("funciono\n\n")
        time.sleep(random.choice([60,120,180,200,500,300,150,20,200,250,80,90,50,10]))
    except Exception as e:
        print("fallo\n\n")
        print(e)
print("espera")

print("el espectador")
print("buscando en google")
links = google.buscar("elespectador")
print("filtrando")
filtredLinks = elespectador.filtro_Autor(links)
for link in filtredLinks:
    print(f"procesando:{link}")
    try:
        dato = elespectador.procesar(link)
        escritor.txt(dato)
        escritor.Json(dato)
        print("funciono\n\n")
        time.sleep(random.choice([60,120,180,200,250,200,500,300,150,2080,90,50,10]))
    except Exception as e:
        print("fallo\n\n")
        print(e)



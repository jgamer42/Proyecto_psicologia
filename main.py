from src.components import google,escritor
import src.components.spiders.eltiempo as eltiempo
import src.components.spiders.elespectador as elespectador
import time
import random
print("el tiempo")
print("buscando en google")
links = google.buscar("eltiempo")
print("filtrando")
filtredLinks = eltiempo.filtro_Autor(links)
for link in filtredLinks:
    print(f"procesando:{link}")
    try:
        dato = eltiempo.procesar(link)
        escritor.txt(dato)
        escritor.Json(dato)
        print("funciono\n\n")
    except:
        print("fallo\n\n")
    finally:
        time.sleep(random.choice([60,120,180]))
print("espera")
time.sleep(180)

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
    except:
        print("fallo\n\n")
    finally:
        time.sleep(random.choice([60,120,180]))



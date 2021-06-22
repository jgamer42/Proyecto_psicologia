from src.buscar_google import buscador
import src.spiders.eltiempo as eltiempo
import escritor

print("buscando en google")
links = buscador("eltiempo")
print("filtrando")
filtredLinks = eltiempo.filtro_Autor(links)
print("procesando")
for link in filtredLinks:
    dato = eltiempo.procesar(link)
    escritor.txt(dato)
    escritor.Json(dato)



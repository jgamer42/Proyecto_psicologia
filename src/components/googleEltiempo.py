from googlesearch import search
import urllib
def buscar():
    site = f"https://www.eltiempo.com/politica/proceso-de-paz"
    palabra = "acuerdos de paz"
    query = f"site:{site} {palabra} after:2014 "
    salida = []
    try:
        data = search(query,tld="com",lang="es",pause=120.0,stop=None)
        for i in data:
            salida.append(i)
    except(urllib.error.HTTPError):
        print("error de request")
    except:
        print("otro")
    finally:
        return salida

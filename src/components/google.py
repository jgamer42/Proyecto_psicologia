from googlesearch import search
import urllib
def buscar(pagina):
    site = f"https://www.{pagina}.com/politica/"
    palabra = "acuerdos de paz"
    query = f"site:{site} {palabra} after:2015 before:2020"
    salida = []
    try:
        data = search(query,tld="com",lang="es",pause=30.0,stop=None)
        for i in data:
            salida.append(i)
    except(urllib.error.HTTPError):
        print("error de request")
    except:
        print("otro")
    finally:
        return salida
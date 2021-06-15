from googlesearch import search
import urllib
def buscador(pagina):
    site = f"https://www.{pagina}.com/politica/"
    palabra = "conficto"
    query = f"site:{site} {palabra} after:2015"
    salida = []
    try:
        data = search(query,tld="com",lang="es",pause=3.0,stop=None)
        for i in data:
            print(i)
            salida.append(i)
    except(urllib.error.HTTPError):
        print("error de request")
    except:
        print("otro")
    finally:
        return salida
buscador("elespectador")
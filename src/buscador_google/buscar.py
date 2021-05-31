from googlesearch import search
import urllib
palabra = "conflicto armado"
site1 = "https://www.elespectador.com/politica/"
site2 = "https://www.eltiempo.com/politica/"
query = f"site:{site1} {palabra} before:2015"
try:
    data = search(query,tld="com",lang="es",pause=3.0,stop=None)
    for i in data:
        print(i)
except(urllib.error.HTTPError):
    print("error de request")
except:
    print("otro")
from googlesearch import search 
query = "site:https://www.eltiempo.com conflicto armado"
data = search(query,tld="com",lang="es",pause=1.0,stop=None)
print(data)
for i in data:
    print(i)
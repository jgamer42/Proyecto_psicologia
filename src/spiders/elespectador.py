import requests
from lxml import html
def elespectador(link):
    salida = {}
    data = requests.get(link)
    data = data.text
    loaded_html = html.fromstring(data)
    titulo = loaded_html.xpath("//div/h1/text()")
    autor = list(set(loaded_html.xpath("//div/div[@class='author_data']/span[@class='who']/text()")))[0]
    print(autor)
    return salida 

elespectador("https://www.eltiempo.com/politica/proceso-de-paz/persiste-la-violencia-en-78-municipios-donde-operaba-las-farc-227184")
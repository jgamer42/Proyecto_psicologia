#from fpdf import FPDF,HTMLMixin
import os
import pandas as pd
import numpy as np
import pdfkit

#class pdf_helper(FPDF,HTMLMixin):
#    pass



base = "/home/jaime/cosas/codigo/proyecto_psicologia/src/components"
ubicacion_archivos = f"{base}/salida"
archivos = os.listdir(ubicacion_archivos)
escribir = ""
for archivo in archivos:
    nombre = archivo.split(".")[0]
    data = pd.read_csv(f"{ubicacion_archivos}/{archivo}")

    a = data.to_html()
    a = f"<h1>{archivo}</h1>"+a
    a = a +f"<img src='{base}/imgs/{nombre}.jpg'/>"
    escribir = escribir + a

c = open("salida.html","w+")
c.write(escribir)
c.close()
pdfkit.from_file("salida.html","salida.pdf")


def normalizar(fecha):
    aux = fecha.split(" ")
    if "de" in aux:
        return formato2(aux)
    else:
        return formato1(aux)

def formato1(fecha):
    if fecha[1] == "Dec":
        mes = 12  
    elif fecha[1] == "Nov":
        mes = 11
    elif fecha[1] == "Oct":
        mes = 10
    elif fecha[1] == "Sep":
        mes = 9
    elif fecha[1] == "Aug":
        mes = 8
    elif fecha[1] == "Jul":
        mes = 7
    elif fecha[1] == "June":
        mes = 6
    elif fecha[1] == "May":
        mes = 5
    elif fecha[1] == "Apr":
        mes = 4
    elif fecha[1] == "Mar":
        mes = 3
    elif fecha[1] == "Feb":
        mes = 2
    elif fecha[1] == "Jan":
        mes = 1
    salida = f"{fecha[0]}/{mes}/{fecha[2]}"
    return salida

def formato2(fecha):
    if fecha[2] == "diciembre":
        mes = 12  
    elif fecha[2] == "noviembre":
        mes = 11
    elif fecha[2] == "octubre":
        mes = 10
    elif fecha[2] == "septiembre":
        mes = 9
    elif fecha[2] == "agosto":
        mes = 8
    elif fecha[2] == "julio":
        mes = 7
    elif fecha[2] == "junio":
        mes = 6
    elif fecha[2] == "mayo":
        mes = 5
    elif fecha[2] == "abril":
        mes = 4
    elif fecha[2] == "marzo":
        mes = 3
    elif fecha[2] == "febrero":
        mes = 2
    elif fecha[2] == "enero":
        mes = 1
    salida = f"{fecha[0]}/{mes}/{fecha[3]}"
    return salida
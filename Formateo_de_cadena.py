def formatear_cadena(cad, ancho=120):
    resp = []
    cad_list = cad.split(" ")
    temp = ""
    cadena=""
    longitud = len(cad_list)
    for i in range(longitud):
        if(len(temp) < ancho):
            temp = temp + cad_list[i]
            temp = temp + " "
        else:
            resp.append(temp)
            temp = ""
            temp = temp + cad_list[i]
            temp = temp + " "
    resp.append(temp)
    for i in range(len(resp)):
        resp[i] = resp[i].strip()
    cadena= "\n".join(resp)
    return cadena

print(formatear_cadena("En un lugar de la mancha, de cuyo nombre no quiero acordarme", 9))


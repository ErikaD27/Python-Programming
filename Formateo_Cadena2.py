def formatear(cadena,ancho):
    lista = cadena.split(" ")
    temp, resultado, res = "", "", []
    for i in lista:
        if len(temp)< ancho:
            temp += i
            temp += " "
        else:
            res.append(temp.strip())
            temp = ""
            temp = temp+i
            temp = temp+" "
    res.append(temp.strip())
    resultado = "\n".join(res)
    return resultado

print(formatear("En un lugar de la Mancha, de cuyo nombre no quiero acordarme",9))
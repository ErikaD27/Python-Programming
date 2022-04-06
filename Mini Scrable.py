def Scrable(palabra,mult = 1,**p):
  sumar,cont = 0,0
  for i in palabra:
    try:
      cont = cont+1
      sumar = sumar+p[i]
    except:
      print("la letra "+palabra[i]+"no tiene puntuación asociada")
  return sumar*mult

print(Scrable("NOAX",N=1,O=1,A=1,X=8))
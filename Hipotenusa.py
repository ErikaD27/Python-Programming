import math
cat1 = int(input("Ingrese el cateto 1"))
cat2 = int(input("Ingrese el cateto 2"))

def hipotenusa():
    hipo= math.sqrt((cat1**2)+(cat2**2))
    return hipo
print(hipotenusa())
#print("la hipotenusa es",h)                                                                                                                                                                                                                                       
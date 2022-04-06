# Tipo de interés (en %, sobre 1)
i = 0.015

# Periodo (en años)
n = 10

# Comisiones mensuales (en €)
f = 5
for C in range(0,20005,5):
  M=C*((1+i)**n)
  G=f*12*n
  S=M-G
  if C<=S:
    print(str(C)+" dicha cantidad de capital aportado es la mínima para no acarrear pérdidas.")
    break
if S<C:
  print(str(C)+" esta cantidad genera perdidas")
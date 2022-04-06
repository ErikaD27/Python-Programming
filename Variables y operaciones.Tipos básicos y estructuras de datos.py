####### ESCRIBE EL CÓDIGO AQUÍ (3 líneas)

c=3000
i=0.015
n=5
M=c*((1+i)**n)

print(f"El capital final es de {M:.2f} €")
f=5
G=5*n*12

print(f"El gasto total en comisiones es de {G:.2f} €")
S=M-G

print(f"El saldo en cuenta tras {n} años es de {S:.2f} €")

hay_ahorro=S>c

print(f"¿Hemos incrementado nuestro capital al finalizar el periodo? -> {hay_ahorro}")
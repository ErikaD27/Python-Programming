
f=open("estaturas.txt","r")
estaturas = []
for linea in f.readlines():
  estaturas.append(float(linea))
print(estaturas)

print(f"la muestra tiene {len(estaturas)}\n La estatura mínima es de {min(estaturas)} m. y la máxima es de {max(estaturas)}m.")

estatura_media = sum(estaturas)/45
print(f" la estatura media {estatura_media:.2f}")

primera = 0
for i in estaturas:
  primera = primera + ((i-estatura_media)**2)
desviacion_tipica = (primera/44)**(0.5)
print(f"la desviación típica es {desviacion_tipica:.3f}")

est_usuario = float(input("Ingrese su altura "))
print(estatura_media)
if est_usuario > estatura_media:
  print(f"Mides {(est_usuario-estatura_media)*100:.0f} cm más que la media")
if est_usuario<estatura_media:
  print(f"Mides {(estatura_media-est_usuario)*100:.0f} cm menos que la media")
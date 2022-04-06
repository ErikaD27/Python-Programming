
lista_clase = ["Juan González","María Moreno","Julia Sánchez","Pedro Vidal"]
notas = []

notas.append((7.5,6.2,8.1))
notas.append((9.3,7.4,7.7))
notas.append((5.6,4.1,4.4))
notas.append((3.8,4.1,6.4))

notas_medias = {lista_clase[0]:(sum(notas[0]))/3,lista_clase[1]:(sum(notas[1]))/3,lista_clase[2]:(sum(notas[2]))/3,lista_clase[3]:(sum(notas[3]))/3}

for nombre, nota_media in notas_medias.items():
    print(f"La nota media de {nombre} es un {nota_media:.1f}.")
aprobados = {lista_clase[0]:((sum(notas[0]))/3)>=5,lista_clase[1]:((sum(notas[1]))/3)>=5,lista_clase[2]:((sum(notas[2]))/3)>=5,lista_clase[3]:((sum(notas[3]))/3)>=5}

print(f"En total han aprobado {sum(aprobados.values())} estudiantes.")
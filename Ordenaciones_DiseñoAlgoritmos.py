l = [7, 1, 4, 3, 9, 11, 5]

print(f"La lista ordenada es: {sorted(l)}")

l = [7, 1, 4, 3, 9, 11, 5]
l.sort()

print(f"La lista ordenada es: {l}")

def esta_ordenada(l):
  lista = sorted(l)
  if lista==l:
    return True
  return False

l1 = [5, 2, 1, 6, 3, 4]
l2 = sorted(l1)

print(f"¿La lista {l1} está ordenada?: {esta_ordenada(l1)}")
print(f"¿La lista {l2} está ordenada?: {esta_ordenada(l2)}")

lis = [8,1,2,4]
def ordenar(l):
  lis = l
  for i in range(1,len(lis)):
    valor = lis[i]
    j=i-1
    while j>=0 and lis[j]>valor:
      lis[j+1]=lis[j]
      j = j-1
    lis[j+1] = valor
  return lis

l = [5, 2, 1, 6, 3, 4]
l = ordenar(l)

print(f"La lista ordenada es: {l}")

def invertir(l):
  lis2 = []
  i = 1
  while i<=len(l):
    lis2.append(l[len(l)-i])
    i = i+1
  return lis2

l = [5, 2, 1, 6, 3, 4]
l = invertir(l)

print(f"La lista invertida es: {l}")

lista = [1, 6, 2, 0, 3, 7, 8, 4, 9, 5]
lista_desc=invertir(ordenar(lista))

print(f"La lista ordenada de mayor a menor es: {lista_desc}")
l = [7, 1, 4, 3, 8, 11, 5,6]


def busca_lineal(l,elemento):
  i,T=0,False
  while i<len(l) and T==False :
    if l[i]==elemento:
      T = True
    else:
      i = i+1
  return T

print(f"El elemento 9 está en la lista: {busca_lineal(l, 9)}")
print(f"El elemento 6 está en la lista: {busca_lineal(l, 6)}")
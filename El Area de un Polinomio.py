def poly(x,*c):
  s = 0
  for j in range(len(c)):
    s = s + ((x**j)*c[j])
  return s

z = poly(3,7,2,5,0,1)
print(z)

def integral(a,b,n):
  area = 0
  ancho = (b - a) / n
  for i in range(n):
    alto = poly(a + i * (b - a) / n,-1,2,1)
    area += ancho * alto
  return area
f=integral(0,5,10000)
print(f)
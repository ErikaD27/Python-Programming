def fibonacci_n(n):
  if n==1 or n==2:
    return 1
  else:
    return fibonacci_n(n-2)+fibonacci_n(n-1)
print(fibonacci_n(15))

def fibonacci(l):
  n1 = 1
  n2 = 1
  yield n1
  yield n2
  for i in range(2,l):
    n = n1+ n2
    yield n
    n1 = n2
    n2 = n
f = list(fibonacci(15))
print(f)
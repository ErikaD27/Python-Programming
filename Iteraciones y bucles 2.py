#f-strings
#format %
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-5, 5, 100)
y = x**3 - 3 * x**2 + 3 * x - 4

plt.rcParams['figure.figsize'] = [6, 4]
plt.rcParams['figure.dpi'] = 120
plt.grid(axis='both', color='0.95')
plt.ylim([-60, 60])
plt.plot(x, x*0, 'k')
plt.plot(x, y, 'r')
plt.show()

a = 2
b = 4
E = 1E-8
'''Este es el margen de error máximo que buscamos.

# Recordemos que la función empleada es: x**3 - 3 * x**2 + 3 * x - 4

# En primer lugar, calcularemos el punto medio –m– del intervalo
#### ESCRIBE EL CÓDIGO AQUÍ (1 línea)'''

m=(a+b)/2

'''A continuación, calcularemos el valor de la función en dicho punto medio –f(m).
#### ESCRIBE EL CÓDIGO AQUÍ (1 línea)'''

f_m=(m**3)-(3*(m**2))+(3*m)-4

'''A continuación, iniciaremos un bucle que debe repetirse mientras el error
# sea mayor que E.
# Nota: ¡el error es la diferencia |f(m) - 0| en valor absoluto!
# Puedes calcular el valor absoluto de un número `x` empleando la función `abs(x)`.
'''

'''A continuación, determinaremos el nuevo intervalo.
  # Habrá que modificar el valor de a o el valor de b, en función de si
  # f(m) < 0 o f(m) > 0.
 '''
while abs(f_m)>E:
    if f_m<0:
        a=m
    else:
        b=m


'''Por último, calculamos el nuevo valor de m y de f(m).
  # Nota: se deben reemplazar los valores calculados anteriormente.
  #### ESCRIBE EL CÓDIGO AQUÍ (2 líneas)'''

m=(a+b)/2
f_m=(m**3)-(3*(m**2))+(3*m)-4


'''Para finalizar, imprimiremos el valor calculado para la raíz:'''
print(f"La función se anula en el punto x = {m:.4f}")
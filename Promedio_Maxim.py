x=list(reversed(range(74,1001)))
sumatoria=0
for i in x:
    if i%2==0:
        print(i)
        sumatoria=sumatoria+i
print(sumatoria)
print(f"El valor promedio es {sumatoria/len(x):.4f}\n El valor minimo es {min(x)}\n el valor máximo es {max(x)}")


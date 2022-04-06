from PIL import Image
import requests
import yfinance
import itranslate

def consulta_tickers():
  tickers = input("Introduzca los tickers separados por comas ")
  tickers_trans = tickers.replace(","," ")
  return tickers_trans
consulta_tickers()

def consulta_periodo():
  periodo = input("Introduzca el periodo para el que quiere consultar la variación ").upper()
  while periodo!= 'Y' and periodo!='M' and periodo!='D':
    periodo = input("Introduzca el periodo para el que quiere consultar la variación ").upper()
  if periodo == 'Y':
    print(f"El valor del periodo es de Año y corresponde al valor: {periodo} ")
  elif periodo == 'M':
    print(f"El valor del periodo es de Mes y corresponde al valor: {periodo} ")
  elif periodo == 'D':
    print(f"El valor del periodo es de Día y corresponde al valor: {periodo} ")
  else:
    print("La opción introducida no es válida. Las opciones válidas son 'Y'(año),'M(mes),'D'(día) ")

consulta_periodo()
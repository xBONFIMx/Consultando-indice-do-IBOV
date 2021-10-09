from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt


#Consultar valor da ação
papel = str(input("Informe o código da ação que deseja consultar: "))
data = str(input('Informe a data que deseja consultar DD-MM-AAAA : '))
valor_papel = web.DataReader(papel, data_source='yahoo', start= data, end = data)

print(valor_papel) #exibe resultado


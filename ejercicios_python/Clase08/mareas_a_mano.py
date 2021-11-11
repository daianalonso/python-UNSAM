#%% Ejercicio 8.10
import pandas as pd

#Que tome como indice el instante en el que se tomó la muestra, y que lo interprete como un timestamp
df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)

#Hacemos una copia de los datos a partir de esta fecha
dh = df['12-25-2014':].copy()

delta_t = 0 # tiempo que tarda la marea entre ambos puertos
delta_h = 0 # diferencia de los ceros de escala entre ambos puertos
#Busco los valores de delta_t entero y delta_h float que hacen que los dos gráficos 
#se vean lo más similares posible, probando a mano
delta_t = -1
delta_h = 22
#Nivelamos las escalas y graficamos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()

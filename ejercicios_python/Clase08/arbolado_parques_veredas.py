#%%Ejercicio 8.9
#Queremos estudiar si hay diferencias entre los ejemplares de una misma especie según si crecen en un sitio
# o en otro
import pandas as pd 
import os

directorio = '../Data'
ruta_arbolado_parques = 'arbolado-en-espacios-verdes.csv'
ruta_arbolado_veredas = 'arbolado-publico-lineal-2017-2018.csv'
fname_arbolado = os.path.join(directorio, ruta_arbolado_parques)
fname_arbolado_lineal = os.path.join(directorio, ruta_arbolado_veredas)

df_parques = pd.read_csv(fname_arbolado)
df_veredas =  pd.read_csv(fname_arbolado_lineal)

#Copio los datos para no modificar los dataframe originales
df_tipas_parques = df_parques[['nombre_cie', 'diametro', 'altura_tot']].copy()
df_tipas_veredas = df_veredas[['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']].copy()

#Renombro columnas para que se llamen igual en ambos dataframe
df_tipas_parques.rename(columns= {'nombre_cie':'nombre_cientifico', 'diametro':'diametro_altura_pecho', 'altura_tot':'altura_arbol'}, inplace=True)

#Agrego columnas en cada dataframe para indicar si corresponden a datos de parques o veredas
df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'

#Combino ambos dataframes en uno
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente')
df_tipas.boxplot('altura_arbol', by='ambiente')

# %%

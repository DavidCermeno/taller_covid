# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 23:50:11 2020

@author: Licht
"""
import pandas as pd
import numpy as np

url = "Casos_positivos_de_COVID-19_en_Colombia.csv"
data = pd.read_csv(url)

data.drop(['Nombre del grupo étnico', 'Pertenencia étnica',
           'Tipo de recuperación', 'Nombre del país',
           'Código ISO del país'], axis=1, inplace=True)


data.loc[data['Ubicación del caso'] ==
         'CASA', 'Ubicación del caso'] = 'Casa'

data.loc[data['Ubicación del caso'] ==
         'casa', 'Ubicación del caso'] = 'Casa'
data.loc[data['Estado'] == 'leve', 'Estado'] = 'Leve'
data.loc[data['Estado'] == 'LEVE', 'Estado'] = 'Leve'
data.loc[data['Recuperado'] == 'fallecido', 'Recuperado'] = 'Fallecido'
data.loc[data['Nombre departamento'] == 'BARRANQUILLA',
         'Nombre departamento'] = 'ATLANTICO'
data.loc[data['Nombre departamento'] == 'CARTAGENA',
         'Nombre departamento'] = 'BOLIVAR'
data.loc[data['Nombre departamento'] == 'STA MARTA D.E.',
         'Nombre departamento'] = 'ATLANTICO'

# 1. Número de casos de Contagiados en el País.

c = data[data['Ubicación del caso'] == 'Casa'].shape[0]
h = data[data['Ubicación del caso'] == 'Hospital'].shape[0]
hu = data[data['Ubicación del caso'] == 'Hospital UCI'].shape[0]
f = data[data['Ubicación del caso'] == 'Fallecido'].shape[0]
g = c + h + hu + f
print(f'El número de casos de Contagiados en colombia es de: {g}')

# 2. Número de Municipios Afectados

ma = data.groupby('Nombre municipio').size()
print(f'El número de municipios afectados en el país es de: {len(ma)}')

# Punto 3: Liste los municipios afectados (sin repetirlos)


# 4. Número de personas que se encuentran en atención en casa

ac = data[data['Ubicación del caso'] == 'Casa'].shape[0]
print(f'La cantidad de personas atendidas en casa es de: {ac}')

# Punto 5: Número de personas que se encuentran recuperados

r = data[data['Recuperado'] == 'Recuperado'].shape[0]
print(f'El número de personas recuperadas es: {r}')

# 6. Número de personas que ha fallecido

f = data[data['Recuperado'] == 'Fallecido'].shape[0]
print(f'El número de personas que han fallecido es: {f}')

# 7. Ordenar de Mayor a menor por tipo de caso (Importado, en estudio,
# Relacionado)

tc = data.groupby('Tipo de contagio').size().sort_values(ascending=False)
print(f'Tipos de casos ordenados de Mayor a menor:\n{tc}')

# 8. Número de departamentos afectados

nda = data.groupby('Nombre departamento').size()
print(f'La cantidad de departamentos afectados es de: {len(nda)}')

# 9. Liste los departamentos afectados(sin repetirlos)

nd = data['Nombre departamento'].unique().tolist()
print(f'Nombre de departamentos sin repetir:\n{nd}')

# 10. Ordene de mayor a menor por tipo de atención


# 11. Liste de mayor a menor los 10 departamentos con mas casos de contagiados

dmcc = data.groupby('Nombre departamento').size().sort_values(ascending=False).head(10)
print(f'Lista de los 10 departamentos con más casos de contagio:\n{dmcc}')

# 12. Liste de mayor a menor los 10 departamentos con mas casos de fallecidos

dmcf = data[data['Estado'] == 'Fallecido']['Nombre departamento'].value_counts().head(10)
print(f'Lista de los 10 departamentos con más casos de fallecidos de mayor a menor:\n{dmcf}')

# 13. Liste de mayor a menor los 10 departamentos con mas casos de recuperados

dmcr = data[data['Recuperado'] == 'Recuperado']['Nombre departamento'].value_counts().head(10)
print(f'Lista de los 10 departartamentos con más casos de recuperados de mayor a menor:\n{dmcr}')

# 14. Liste de mayor a menor los 10 municipios con mas casos de contagiados

mmc = data.groupby('Nombre municipio').size().sort_values(ascending=False).head(10)
print(f'Lista de municipios contagiados:\n{mmc}')


# 15. Liste de mayor a menor los 10 municipios con mas casos de fallecidos

mmcf = data[data['Estado'] =='Fallecido']['Nombre municipio'].value_counts(ascending = False).head(10)
print(f'Lista de municipio con más casos de facellidos:\n{mmcf}')

# 16. Liste de mayor a menor los 10 municipios con mas casos de recuperados

mcmr = data[data['Recuperado'] == 'Recuperado']['Nombre municipio'].value_counts(ascending=False).head(10)
print(f'Lista de los 10 municipios con más casos de recuperados de mayor a menor:\n{mcmr}')

# 21. Liste de mayor a menor las fechas donde se presentaron mas
# contagios

fmc = data.groupby('Fecha de inicio de síntomas').size().sort_values(ascending=False)
print(f'Lista de fechas de contagiados de mayor a menor:\n{fmc}')

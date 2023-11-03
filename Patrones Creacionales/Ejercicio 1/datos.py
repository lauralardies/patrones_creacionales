import pandas as pd

url = 'https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv'

# Cargamos el fichero CSV en un dataframe leyendo desde la url
data = pd.read_csv(url, sep=';', encoding='ISO-8859-1')

# Mostramos las 5 primeras filas
print(data.head())
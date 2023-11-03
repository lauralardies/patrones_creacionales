import pandas as pd

url = 'https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv'

# Cargamos el fichero CSV en un dataframe leyendo desde la url
data = pd.read_csv(url, sep=';', encoding='ISO-8859-1')

# Mostramos las 5 primeras filas
print('Dataframe original, de tamaño {}:'.format(data.shape)) # Comprobamos el tamaño del dataset --> (18, 30)
print(data.head()) # De esta forma podemos ver la estructura de los datos

# ----------------------------------------------------------
# Limpieza de datos
# ----------------------------------------------------------

# Eliminamos las filas que tienen valores nulos
columnas_basura = ['PRECIO', 'DIAS-EXCLUIDOS', 'DESCRIPCION', 'AUDIENCIA', 'Unnamed: 29']
data_limpio = data.drop(columns=columnas_basura)

print('\nDataframe limpio, de tamaño {}:'.format(data_limpio.shape))
print(data_limpio.head())

# No aplicamos dropna() para eliminar filas con valores nulos porque de lo contrario, vaciamos el dataframe
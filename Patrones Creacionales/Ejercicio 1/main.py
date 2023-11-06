from abstract_factory import AbstractFactory
import pandas as pd


def client_code(factory: AbstractFactory) -> None:

    # Cargamos los datos del csv en la carpeta data
    data = pd.read_csv('Patrones Creacionales/Ejercicio 1/data/data_limpio.csv', sep=';', encoding='ISO-8859-1')

    # Volvemos a convertir las columnas FECHA y FECHA-FIN a tipo datetime
    data['FECHA'] = pd.to_datetime(data['FECHA'], errors='coerce')
    data['FECHA-FIN'] = pd.to_datetime(data['FECHA-FIN'], errors='coerce')

    # Porqué vuelvo a hacer transformación de datos?
    # Los archivos CSV, como formato de almacenamiento de datos, no incluyen información 
    # sobre el tipo de datos de cada columna. Cuando guardas un DataFrame en un archivo CSV, 
    # los datos se guardan sin la información de los tipos de datos, lo que significa que 
    # cuando vuelves a cargar el DataFrame, el programa debe inferir los tipos de datos en 
    # función de los datos almacenados en el CSV.

    columna = 'FECHA' # Columna que queremos analizar

    analisis_estadistico = factory.crear_analisis_estadistico()
    visualizacon_graficas = factory.crear_graficas()

    if visualizacon_graficas is None:
        print(f"\nMedia: \n{analisis_estadistico.calcular_media(data, columna)}")
        print(f"\nMediana: \n{analisis_estadistico.calcular_mediana(data, columna)}")
        print(f"\nModa: \n{analisis_estadistico.calcular_moda(data, columna)}")
    elif analisis_estadistico is None:
        visualizacon_graficas.mostrar_histograma(data, columna)
        visualizacon_graficas.mostrar_diagrama_barras(data, columna)
    else:
        pass
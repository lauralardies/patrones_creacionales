from __future__ import annotations
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import pandas as pd


class AbstractFactory(ABC):

    @abstractmethod
    def crear_analisis_estadistico(self) -> AbstractAnalisis:
        pass

    @abstractmethod
    def crear_graficas(self) -> AbstractGrafica:
        pass


class ConcreteAnalisisFactory(AbstractFactory):

    def crear_analisis_estadistico(self) -> AbstractAnalisis:
        return Analisis()

    def crear_graficas(self) -> AbstractGrafica:
        return None # No se implementa en este caso


class ConcreteGraficasFactory(AbstractFactory):

    def crear_analisis_estadistico(self) -> AbstractAnalisis:
        return None # No se implementa en este caso

    def crear_graficas(self) -> AbstractGrafica:
        return Grafica()


class AbstractAnalisis(ABC):
    @abstractmethod
    def calcular_media(self, data, columna):
        pass
    
    def calcular_mediana(self, data, columna):
        pass

    def calcular_moda(self, data, columna):
        pass


class Analisis(AbstractAnalisis):

    def calcular_media(self, data, columna):
        val = data[columna]
        if data[columna].dtypes == 'datetime64[ns]' or data[columna].dtypes == 'M8[ns]':
            val = data.groupby(data[columna].dt.date).size()
        return val.mean()

    def calcular_mediana(self, data, columna):
        val = data[columna]
        if data[columna].dtypes == 'datetime64[ns]' or data[columna].dtypes == 'M8[ns]':
            val = data.groupby(data[columna].dt.date).size()
        return val.median()

    def calcular_moda(self, data, columna):
        val = data[columna]
        if data[columna].dtypes == 'datetime64[ns]' or data[columna].dtypes == 'M8[ns]':
            val = data.groupby(data[columna].dt.date).size()
        mode_val = val.value_counts()
        return mode_val.idxmax()


class AbstractGrafica(ABC):
    @abstractmethod
    def mostrar_histograma(self, data, columna):
        pass

    def mostrar_diagrama_barras(self, data, columna):
        pass


class Grafica(AbstractGrafica):
    def mostrar_histograma(self, data, columna):
        val = data[columna]
        if data[columna].dtypes == 'datetime64[ns]' or data[columna].dtypes == 'M8[ns]':
            val = data.groupby(data[columna].dt.date).size()
        val.plot(kind='hist')
        plt.show()

    def mostrar_diagrama_barras(self, data, columna):
        val = data[columna]
        if data[columna].dtypes == 'datetime64[ns]' or data[columna].dtypes == 'M8[ns]':
            val = data.groupby(data[columna].dt.date).size()
        val.plot(kind='bar')
        plt.show()


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


if __name__ == "__main__":    

    print("Client: Testing la factoría de Análisis Estadísticos:")
    client_code(ConcreteAnalisisFactory())

    print("\nClient: Testing la factoría de Visualización de Datos:")
    client_code(ConcreteGraficasFactory())
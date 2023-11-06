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
    def calcular_media(self, data):
        pass
    
    def calcular_mediana(self, data):
        pass

    def calcular_moda(self, data):
        pass


class Analisis(AbstractAnalisis):

    def calcular_media(self, data):
        return data.mean()

    def calcular_mediana(self, data):
        return data.median()

    def calcular_moda(self, data):
        mode_data = data.value_counts()
        return mode_data.idxmax()


class AbstractGrafica(ABC):
    @abstractmethod
    def mostrar_histograma(self, data):
        pass

    def mostrar_diagrama_barras(self, data):
        pass


class Grafica(AbstractGrafica):
    def mostrar_histograma(self, data):
        data.plot(kind='hist')
        plt.show()

    def mostrar_diagrama_barras(self, data):
        data.plot(kind='bar')
        plt.show()


def client_code(factory: AbstractFactory) -> None:

    # Cargamos los datos del csv en la carpeta data
    data = pd.read_csv('Patrones Creacionales/Ejercicio 1/data/data_limpio.csv', sep=';', encoding='ISO-8859-1')
    columna = 'LATITUD' # Columna que queremos analizar

    analisis_estadistico = factory.crear_analisis_estadistico()
    visualizacon_graficas = factory.crear_graficas()

    if visualizacon_graficas is None:
        print(f"\nMedia: \n{analisis_estadistico.calcular_media(data[columna])}")
        print(f"\nMediana: \n{analisis_estadistico.calcular_mediana(data[columna])}")
        print(f"\nModa: \n{analisis_estadistico.calcular_moda(data[columna])}")
    elif analisis_estadistico is None:
        visualizacon_graficas.mostrar_histograma(data[columna])
        visualizacon_graficas.mostrar_diagrama_barras(data[columna])
    else:
        pass


if __name__ == "__main__":
   
    print("Client: Testing la factoría de Análisis Estadísticos:")
    client_code(ConcreteAnalisisFactory())

    print("\nClient: Testing la factoría de Visualización de Datos:")
    client_code(ConcreteGraficasFactory())
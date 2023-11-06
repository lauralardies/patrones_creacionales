from __future__ import annotations
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


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
        plt.savefig('Patrones Creacionales/Ejercicio 1/graficas/histograma.png')

    def mostrar_diagrama_barras(self, data, columna):
        val = data[columna]
        if data[columna].dtypes == 'datetime64[ns]' or data[columna].dtypes == 'M8[ns]':
            val = data.groupby(data[columna].dt.date).size()
        val.plot(kind='bar')
        plt.savefig('Patrones Creacionales/Ejercicio 1/graficas/diagramabarras.png')
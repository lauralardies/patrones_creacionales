from __future__ import annotations
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


class GraficasFactory(ABC):
    """
    Interfaz para visualización de gráficas. Declaramos una serie de métodos: histograma
    y diagrama de barras, que devuelven diferentes productos abstractos.
    """

    @abstractmethod
    def crear_histograma(self) -> AbstractGrafica:
        pass

    @abstractmethod
    def crear_diagrama_barras(self) -> AbstractGrafica:
        pass

# Factoría concreta para visualiazciones gráficas
class ConcreteGraficasFactory(GraficasFactory):

    def crear_histograma(self) -> Histograma:
        return Histograma()

    def crear_diagrama_barras(self) -> DiagramaBarras:
        return DiagramaBarras()


class AbstractGrafica(ABC):
    @abstractmethod
    def mostrar(self, data):
        pass


class Histograma(AbstractGrafica):
    def mostrar(self, data):
        data.plot(kind='hist')
        plt.show()


class DiagramaBarras(AbstractGrafica):
    def mostrar(self, data):
        data.plot(kind='bar')
        plt.show()

from __future__ import annotations
from abc import ABC, abstractmethod


class AnalisisEstadisticoFactory(ABC):
    """
    Interfaz para análisis estadísticos. Declaramos una serie de métodos: media, mediana 
    y moda, que devuelven diferentes productos abstractos.
    """

    @abstractmethod
    def crear_media(self) -> AbstractAnalisis:
        pass

    @abstractmethod
    def crear_mediana(self) -> AbstractAnalisis:
        pass
    
    @abstractmethod
    def crear_moda(self) -> AbstractAnalisis:
        pass


# Factoría concreta para análisis estadísticos
class ConcreteAnalisisFactory(AnalisisEstadisticoFactory):

    def crear_media(self) -> Media:
        return Media()

    def crear_mediana(self) -> Mediana:
        return Mediana()

    def crear_moda(self) -> Moda:
        return Moda()


class AbstractAnalisis(ABC):
    @abstractmethod
    def calcular(self):
        pass


class Media(AbstractAnalisis):
    def calcular(self, data):
        return data.mean()


class Mediana(AbstractAnalisis):
    def calcular(self, data):
        return data.median()


class Moda(AbstractAnalisis):
    def calcular(self, data):
        mode_data = data.value_counts()
        return mode_data.idxmax()
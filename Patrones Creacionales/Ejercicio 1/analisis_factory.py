from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd

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

    def crear_media(self) -> AbstractAnalisis:
        return Media()

    def crear_mediana(self) -> AbstractAnalisis:
        return Mediana()

    def crear_moda(self) -> AbstractAnalisis:
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
        return data.mode()

def client_code(factory: AnalisisEstadisticoFactory) -> None:
    
    # Cargamos los datos del csv en la carpeta data
    data = pd.read_csv('Patrones Creacionales/Ejercicio 1/data/data_limpio.csv', sep=';', encoding='ISO-8859-1')

    media = factory.crear_media()
    mediana = factory.crear_mediana()
    moda = factory.crear_moda()

    print(f"Media: {media.calcular(data)}")
    print(f"Mediana: {mediana.calcular(data)}")
    print(f"Moda: {moda.calcular(data)}")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing la factoría:")
    client_code(ConcreteAnalisisFactory())
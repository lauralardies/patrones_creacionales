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
        mode_data = data.value_counts()
        return mode_data.idxmax()

def client_code(factory: AnalisisEstadisticoFactory) -> None:
    
    # Cargamos los datos del csv en la carpeta data
    data = pd.read_csv('Patrones Creacionales/Ejercicio 1/data/data_limpio.csv', sep=';', encoding='ISO-8859-1')
    columna = 'LATITUD' # Columna que queremos analizar

    media = factory.crear_media()
    mediana = factory.crear_mediana()
    moda = factory.crear_moda()

    print(f"\nMedia: \n{media.calcular(data[columna])}")
    print(f"\nMediana: \n{mediana.calcular(data[columna])}")
    print(f"\nModa: \n{moda.calcular(data[columna])}")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing la factoría:")
    client_code(ConcreteAnalisisFactory())
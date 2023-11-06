from analisis_factory import *
from graficas_factory import *
import pandas as pd

def client_code(factory: AbstractFactory) -> None:
    
    # Cargamos los datos del csv en la carpeta data
    data = pd.read_csv('Patrones Creacionales/Ejercicio 1/data/data_limpio.csv', sep=';', encoding='ISO-8859-1')
    columna = 'LATITUD' # Columna que queremos analizar

    media = factory.crear_media()
    mediana = factory.crear_mediana()
    moda = factory.crear_moda()

    print(f"\nMedia: \n{media.calcular(data[columna])}")
    print(f"\nMediana: \n{mediana.calcular(data[columna])}")
    print(f"\nModa: \n{moda.calcular(data[columna])}")

    histograma = factory.crear_histograma()
    diagrama_barras = factory.crear_diagrama_barras()

    histograma.mostrar(data[columna])
    diagrama_barras.mostrar(data[columna])


if __name__ == "__main__":
    print("Client: Testing la factoría de Análisis Estadísticos:")
    client_code(ConcreteAnalisisFactory())

    print("\nClient: Testing la factoría de Visualización de Datos:")
    client_code(ConcreteGraficasFactory())
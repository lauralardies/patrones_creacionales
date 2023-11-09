# Patrones Creacionales

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/patrones_creacionales)
https://github.com/lauralardies/patrones_creacionales

## Enunciados

En esta entrega tenemos que realizar dos ejercicios:

### Ejercicio 1

El SAMUR-Protección Civil es el servicio de atención a urgencias y emergencias sanitarias extrahospitalarias en el municipio de Madrid. Su labor es esencial para garantizar la seguridad y el bienestar de los ciudadanos en situaciones de emergencia. A lo largo del año, el SAMUR lleva a cabo múltiples "activaciones" en respuesta a diversas situaciones, desde accidentes de tráfico hasta emergencias médicas.

La ciudad de Madrid, en su compromiso con la transparencia y la apertura de datos, publica un registro detallado de estas activaciones en formato CSV. Este registro incluye información como la fecha, hora, tipo de emergencia, y otros detalles relevantes de cada activación.

Tu tarea es desarrollar un programa en Python que haga uso del patrón de diseño "Abstract Factory" para modularizar y estandarizar el análisis de estos datos. En específico:

1. Lectura de Datos: Acceda y lea el archivo CSV directamente desde el enlace proporcionado: Activaciones del SAMUR-Protección Civil.
2. Modelado de Datos: Modela y estructura la información para su análisis.
3. Abstract Factory: Diseña un "Abstract Factory" que permita crear diferentes tipos de análisis o representaciones de los datos. Por ejemplo:
   - Una fábrica que genere análisis estadísticos (media, moda, mediana).
   - Una fábrica que produzca visualizaciones gráficas (histogramas, gráficos de barras).
  Cada fábrica debe tener al menos dos productos concretos (e.g., histograma de activaciones por tipo de emergencia, gráfico de barras de activaciones por mes).
4. Análisis y Representación: Utiliza las fábricas creadas para generar distintos análisis y representaciones de los datos. Muestra la media de activaciones por día, y un histograma de las activaciones.


### Ejercicio 2

La reconocida cadena de pizzerías gourmet "Delizioso" ha decidido lanzar una plataforma digital para permitir a sus clientes diseñar y personalizar sus pizzas al máximo detalle. Esta pizzería es conocida por su meticulosidad y su vasto menú de ingredientes, técnicas de cocción y presentaciones. Además de la personalización, "Delizioso" busca almacenar cada pizza diseñada por sus clientes en un archivo CSV para análisis posterior, recomendaciones personalizadas y marketing dirigido.

Características a considerar:

1. Tipo de masa.
2. Salsa base.
3. Ingredientes principales.
4. Técnicas de cocción.
5. Presentación.
6. Maridajes recomendados.
7. Extras y finalizaciones.

Objetivos:

1. Diseñar un sistema que permita a los clientes construir su pizza paso a paso utilizando el patrón Builder.
2. Asegurar que cada elección sea validada para ser compatible con las selecciones previas del cliente.
3. Incorporar un sistema de recomendaciones que sugiera ingredientes, técnicas y maridajes basados en las elecciones previas del cliente.
4. Desarrollar un módulo que guarde cada pizza personalizada en un archivo CSV, almacenando cada detalle, desde los ingredientes hasta el maridaje recomendado.
5. Crear una funcionalidad que lea del archivo CSV y pueda reconstruir la pizza para su visualización, edición o reorden.
6. Garantizar la flexibilidad del sistema para futuras adiciones o modificaciones, ya que la pizzería está en constante innovación.
7. Desarrollar una interfaz de usuario amigable que guíe al cliente en el proceso de creación, ofreciendo información relevante sobre cada elección y facilitando la toma de decisiones.
8. Implementar medidas de seguridad para garantizar la integridad de los datos almacenados y la privacidad de las elecciones de los clientes.

## Archivos

Encontramos todos los archivos en una carpeta llamada `Patrones Creacionales`, donde a su vez podemos encontrar otras dos subcarpetas:
- Carpeta `Ejercicio 1`:
  - Carpeta `data`, donde guardamos en archivo CSV una vez ha sido limpiado y además podemos encontrar un archivo llamado `datos.py`, que es el encargado de analizar los datos y limpiarlos.
  - Carpeta `graficas`, donde almacenamos las gráficas generadas en la visualización de datos.
  - Archivo `main.py`. Aquí generamos el código de cliente.
  - Archivo `run.py`, el lanzador desde el cual se ejecuta todo el programa.
  - Por último, encontramos una serie de archivos que conjuntamente forman un patrón conocido como **Abstract Factory**. Los archivos que forman este patrón son los siguientes:
    - `abstract_factory.py`.
    - `abstract_analisis.py`
    - `abstract_grafica.py`
    - `concrete_analisis_factory.py`
    - `concrete_analisis_factory.py`
    - `analisis.py`
    - `grafica.py`

   > ¿Por qué empleamos el patrón Abstract Factory para este ejercicio?\
   > El patrón Abstract Factory se puede utilizar en este escenario para proporcionar una estructura flexible y escalable para la generación de análisis y representaciones de datos. Dado que se requieren diferentes tipos de análisis y representaciones, el patrón Abstract Factory puede ayudar a crear familias de objetos relacionados sin especificar sus clases concretas.\
   > Al utilizar el patrón Abstract Factory en este caso, puedes modularizar el proceso de generación de análisis y representaciones, lo que facilita la incorporación de nuevos tipos de análisis o representaciones en el futuro sin alterar el código existente. Esto mejora la mantenibilidad y la flexibilidad del programa en general.\
   > Además, dado que el programa necesita realizar múltiples tareas como la lectura de datos, el modelado de datos y la generación de diferentes tipos de análisis y representaciones, el uso del patrón Abstract Factory puede ayudar a mantener una estructura clara y organizada en el código, lo que facilita su comprensión y mantenimiento a largo plazo.
    
- Carpeta `Ejercicio 2`:
  - Carpeta `data`, donde almacenamos las pizzas generadas por el cliente en un archivo CSV.
  - Carpeta `img` que guarda las imágenes empleadas posteriormente para la interfaz gráfica de usuario (GUI).
  - Algunos de los archivos restantes forman conjuntamente un código que construyen el patrón conocido como Builder. Además, incluimos el archivo `main_terminal.py` que une el código del patrón en un único archivo. Los archivos del patrón son los siguientes:
    - `director.py`
    - `builder.py`
    - `pizza_builder.py`
    - `pizza.py`
     En estos archivos también empleamos `config.py` para limpiar la consola cuando lo indiquemos.
  - También encontramos un archivo llamado `gui.py` en el cual desarrollamos una aplicación con la biblioteca Tkinter y la ejecutamos en el fichero `main_tkinter.py`

  
  > ¿Por qué empleamos el patrón Builder para este ejercicio?\
  


## Código

### Ejercicio 1

#### Archivo `datos.py`
```
import pandas as pd

url = 'https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv'

# Cargamos el fichero CSV en un dataframe leyendo desde la url
data = pd.read_csv(url, sep=';', encoding='ISO-8859-1')

# Mostramos las 5 primeras filas
print('Dataframe original, de tamaño {}:'.format(data.shape)) # Comprobamos el tamaño del dataset --> (15, 30)
print(data.head()) # De esta forma podemos ver la estructura de los datos

# ----------------------------------------------------------
# Limpieza de datos
# ----------------------------------------------------------

print(data.isnull().sum()) # Comprobamos el número de valores nulos por columna

# Eliminamos las filas que tienen valores nulos
columnas_basura = ['PRECIO', 'DIAS-EXCLUIDOS', 'HORA', 'DESCRIPCION', 'AUDIENCIA', 'Unnamed: 29']
data_limpio = data.drop(columns=columnas_basura)

print('\nDataframe limpio, de tamaño {}:'.format(data_limpio.shape))
print(data_limpio.head())

# No aplicamos dropna() para eliminar filas con valores nulos porque de lo contrario,
# el dataframe se queda prácticamente vacío

# ----------------------------------------------------------
# Transformación de datos
# ----------------------------------------------------------

print(data_limpio.dtypes) # Comprobamos los tipos de datos de cada columna
# FECHA: object --> datetime64[ns]

# Convertimos las columnas FECHA y FECHA-FIN a tipo datetime
data_limpio['FECHA'] = pd.to_datetime(data_limpio['FECHA'], errors='coerce')
data_limpio['FECHA-FIN'] = pd.to_datetime(data_limpio['FECHA-FIN'], errors='coerce')

print(data_limpio.dtypes) # Comprobamos los tipos de datos de cada columna

# Guardamos el dataframe limpio en un fichero CSV dentro de la carpeta data
data_limpio.to_csv('Patrones Creacionales/Ejercicio 1/data/data_limpio.csv', sep=';', encoding='ISO-8859-1')
```

#### Archivo `main.py`
```
from abstract_factory import AbstractFactory
import pandas as pd


def client_code(factory: AbstractFactory, media = False, mediana = False, moda = False, histograma = False, diagrama_barras = False) -> None:

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
        if media:
            print(f"\nMedia: \n{analisis_estadistico.calcular_media(data, columna)}")
        elif mediana:
            print(f"\nMediana: \n{analisis_estadistico.calcular_mediana(data, columna)}")
        elif moda:
            print(f"\nModa: \n{analisis_estadistico.calcular_moda(data, columna)}")
        else:
            pass

    elif analisis_estadistico is None:
        if histograma:
            visualizacon_graficas.mostrar_histograma(data, columna)
        elif diagrama_barras:
            visualizacon_graficas.mostrar_diagrama_barras(data, columna)
        else:
            pass
    else:
        pass
```

#### Archivo `run.py`
```
from main import client_code
from concrete_analisis_factory import ConcreteAnalisisFactory
from concrete_graficas_factory import ConcreteGraficasFactory


if __name__ == "__main__":    
    
    print('Analizamos las activaciones por día.')

    # Sólo calculamos la media de las activaciones por día y sólo dibujamos el histograma
    client_code(ConcreteAnalisisFactory(), media = True)
    client_code(ConcreteGraficasFactory(), histograma = True)

    print("Las gráficas se han guardado en la carpeta graficas.")
```

#### Archivo `abstract_factory.py`
```
from __future__ import annotations
from abc import ABC, abstractmethod
from abstract_analisis import AbstractAnalisis
from abstract_grafica import AbstractGrafica

class AbstractFactory(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def crear_analisis_estadistico(self) -> AbstractAnalisis:
        pass

    @abstractmethod
    def crear_graficas(self) -> AbstractGrafica:
        pass
```

#### Archivo `abstract_analisis.py`
```
from abc import ABC, abstractmethod

class AbstractAnalisis(ABC):
    
    @abstractmethod
    def calcular_media(self, data, columna):
        pass
    
    def calcular_mediana(self, data, columna):
        pass

    def calcular_moda(self, data, columna):
        pass
```

#### Archivo `abstract_grafica.py`
```
from abc import ABC, abstractmethod

class AbstractGrafica(ABC):
    
    @abstractmethod
    def mostrar_histograma(self, data, columna):
        pass

    def mostrar_diagrama_barras(self, data, columna):
        pass
```

#### Archivo `concrete_analisis_factory.py`
```
from abstract_factory import AbstractFactory
from abstract_analisis import AbstractAnalisis
from abstract_grafica import AbstractGrafica
from analisis import Analisis

class ConcreteAnalisisFactory(AbstractFactory):

    def crear_analisis_estadistico(self) -> AbstractAnalisis:
        return Analisis()

    def crear_graficas(self) -> AbstractGrafica:
        return None # No se implementa en este caso
```

#### Archivo `concrete_graficas_factory.py`
```
from abstract_factory import AbstractFactory
from abstract_analisis import AbstractAnalisis
from abstract_grafica import AbstractGrafica
from grafica import Grafica

class ConcreteGraficasFactory(AbstractFactory):

    def crear_analisis_estadistico(self) -> AbstractAnalisis:
        return None # No se implementa en este caso

    def crear_graficas(self) -> AbstractGrafica:
        return Grafica()
```

#### Archivo `analisis.py`
```
from abstract_analisis import AbstractAnalisis

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
```

#### Archivo `grafica.py`
```
from abstract_grafica import AbstractGrafica    
import matplotlib.pyplot as plt

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
```

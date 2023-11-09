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
    - `abstract_analisis.py`.
    - `abstract_grafica.py`.
    - `concrete_analisis_factory.py`.
    - `concrete_analisis_factory.py`.
    - `analisis.py`.
    - `grafica.py`.


   > **¿Por qué empleamos el patrón Abstract Factory para este ejercicio?**\
   > El patrón Abstract Factory se puede utilizar en este escenario para proporcionar una estructura flexible y escalable para la generación de análisis y representaciones de datos. Dado que se requieren diferentes tipos de análisis y representaciones, el patrón Abstract Factory puede ayudar a crear familias de objetos relacionados sin especificar sus clases concretas.\
   > Al utilizar el patrón Abstract Factory en este caso, puedes modularizar el proceso de generación de análisis y representaciones, lo que facilita la incorporación de nuevos tipos de análisis o representaciones en el futuro sin alterar el código existente. Esto mejora la mantenibilidad y la flexibilidad del programa en general.\
   > Además, dado que el programa necesita realizar múltiples tareas como la lectura de datos, el modelado de datos y la generación de diferentes tipos de análisis y representaciones, el uso del patrón Abstract Factory puede ayudar a mantener una estructura clara y organizada en el código, lo que facilita su comprensión y mantenimiento a largo plazo.
    
- Carpeta `Ejercicio 2`:
  - Carpeta `data`, donde almacenamos las pizzas generadas por el cliente en un archivo CSV.
  - Carpeta `img` que guarda las imágenes empleadas posteriormente para la interfaz gráfica de usuario (GUI).
  - Archivo `main.py` en el cual accedemos a un menú, empleamos una función del archivo `config.py` para limpiar la pantalla de la terminal.
  - Archivo `run.py` que actúa como lanzador.
  - Algunos de los archivos restantes forman conjuntamente un código que construyen el patrón conocido como **Builder**. Además, incluimos el archivo `main_terminal.py` que une el código del patrón en un único archivo. Los archivos del patrón son los siguientes:
    - `director.py`.
    - `builder.py`.
    - `pizza_builder.py`.
    - `pizza.py`.
      
     En estos archivos también empleamos `config.py` para limpiar la consola cuando lo indiquemos.
    
  - También encontramos un archivo llamado `gui.py` en el cual desarrollamos una aplicación con la biblioteca Tkinter y la ejecutamos en el fichero `main_tkinter.py`.
  
  > **¿Por qué empleamos el patrón Builder para este ejercicio?**\
  > En el escenario descrito, el patrón Builder sería adecuado para la implementación del sistema de construcción de pizzas personalizadas. Dado que hay múltiples componentes y pasos involucrados en la creación de una pizza personalizada, el patrón Builder puede facilitar la construcción paso a paso de objetos complejos, como una pizza con todas sus características específicas.\
  > Aquí hay algunas razones por las cuales sería útil emplear el patrón Builder en este ejercicio:\
  > 1. **Construcción paso a paso:** El patrón Builder permite a los clientes construir su pizza paso a paso, seleccionando cada componente a lo largo del camino.\
  > 2. **Validación de selecciones:** El Builder puede asegurar que cada elección sea validada y compatible con las selecciones previas del cliente, evitando combinaciones inválidas.\
  > 3. **Flexibilidad y expansión:** El patrón Builder facilita la incorporación de nuevas características o componentes en la construcción de la pizza sin modificar el código existente, lo que garantiza la flexibilidad del sistema.\
  > 4. **Estructura clara y modular:** El uso del patrón Builder puede proporcionar una estructura clara y modular para la construcción de pizzas personalizadas, lo que facilita el mantenimiento y la comprensión del código a largo plazo.\
  > 5. **Recomendaciones dinámicas:** El sistema de recomendaciones basado en las elecciones previas del cliente puede integrarse fácilmente con el patrón Builder para sugerir ingredientes, técnicas de cocción y maridajes adecuados.\
  > 6. **Separación de preocupaciones:** El patrón Builder permite separar la lógica de construcción de pizza del código de la interfaz de usuario, lo que mejora la claridad y la mantenibilidad del código.\
  > En resumen, el patrón Builder sería útil en este escenario para facilitar la creación de pizzas personalizadas, asegurando la validación de selecciones, la flexibilidad y la modularidad del sistema, así como la implementación de recomendaciones dinámicas basadas en las elecciones de los clientes.

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

### Ejercicio 2

#### Archivo `config.py`
```
import os
import platform

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')
```

#### Archivo `run.py`
```
from main import main


if __name__ == "__main__":
    '''
    Lanzador del programa
    '''
    main()
```

#### Archivo `main.py`
```
from main_terminal import main as main_terminal
from main_tkinter import main as main_tkinter
from config import limpiar_pantalla



def main():

    while True:
        limpiar_pantalla()
        print('Hola! ¿Queres hacer la pizza desde la terminal de tu ordenador o desde una interfaz gráfica?')
        print('1. Terminal')
        print('2. Interfaz gráfica')
        print('3. Salir')
        opcion = input('>> ')
        if opcion == '1':
            main_terminal()
        elif opcion == '2':
            main_tkinter()
        elif opcion == '3':
            break
        else:
            limpiar_pantalla()
            print('Opción inválida')
            input('Presiona cualquier tecla para continuar...')
```

#### Archivo `main_terminal.py`
```
from director import Director
from pizza_builder import PizzaBuilder
from config import limpiar_pantalla


def main():
    '''
    Desde esta función, el cliente podrá acceder a los servicios de la pizzeria desde la terminal
    '''
    director = Director()
    builder = PizzaBuilder()
    director.builder = builder

    while True:
        limpiar_pantalla()
        # Primero pedimos crear la pizza
        print("Crea tu pizza: ")
        director.construir_completo()
        builder.pizza.guardar_csv()

        # Luego mostramos la pizza creada
        limpiar_pantalla()
        print("Tu pizza: ")
        builder.pizza.visualizacion_csv()

        # Finalmente preguntamos si le gusta la pizza
        print("¿Te gusta tu pizza? [Y]/N")
        respuesta = input('>> ')
        limpiar_pantalla()
        if respuesta.capitalize() == 'N': # Si no le gusta, volvemos a empezar
            builder.pizza.borrar_pizza()
            print('Empecemos de nuevo')
            input('Presiona cualquier tecla para continuar...')
        else: # Si le gusta, guardamos la pizza y terminamos
            print('¡Gracias por tu compra!')
            input('Presiona cualquier tecla para continuar...')
            break
```

#### Archivo `main_tkinter.py`
```
import tkinter as tk
from gui import crear_pagina_inicio, crear_pagina_masa, crear_pagina_salsa, crear_pagina_ingredientes, crear_pagina_coccion, crear_pagina_presentacion, crear_pagina_maridaje, crear_pagina_extras, crear_pagina_final
from PIL import Image, ImageTk


def main():

    root = tk.Tk()
    root.title("Personaliza tu pizza")
    root.geometry("1100x600")

    image = Image.open("Patrones Creacionales/Ejercicio 2/img/pizza_index.jpg")  # Cambia la ruta por la ubicación de tu imagen
    background_image = ImageTk.PhotoImage(image)

    # Mostrar la imagen en un widget de etiqueta
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Ajusta la posición y el tamaño de la imagen

    pagina_inicio = crear_pagina_inicio(root)
    pagina_masa = crear_pagina_masa(root)
    pagina_salsa = crear_pagina_salsa(root)
    pagina_ingredientes = crear_pagina_ingredientes(root)
    pagina_coccion = crear_pagina_coccion(root)
    pagina_presentacion = crear_pagina_presentacion(root)
    pagina_maridaje = crear_pagina_maridaje(root)
    pagina_extras = crear_pagina_extras(root)
    pagina_final = crear_pagina_final(root)

    pagina_inicio.pack()

    root.mainloop()
```

#### Archivo `director.py`
```
from builder import Builder


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def construir_completo(self) -> None:
        self.builder.masa()
        self.builder.salsa()
        self.builder.ingredientes()
        self.builder.coccion()
        self.builder.presentacion()
        self.builder.maridajes()
        self.builder.extras()
```

#### Archivo `builder.py`
```
from __future__ import annotations
from abc import ABC, abstractmethod


class Builder(ABC):

    @property
    @abstractmethod
    def pizza(self) -> None:
        pass

    @abstractmethod
    def masa(self) -> None:
        pass

    @abstractmethod
    def salsa(self) -> None:
        pass

    @abstractmethod
    def ingredientes(self) -> None:
        pass

    @abstractmethod
    def coccion(self) -> None:
        pass

    @abstractmethod
    def presentacion(self) -> None:
        pass

    @abstractmethod
    def maridajes(self) -> None:
        pass

    @abstractmethod
    def extras(self) -> None:
        pass
```

#### Archivo `pizza_builder.py`
```
from builder import Builder
from pizza import Pizza

class PizzaBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = Pizza()

    @property
    def pizza(self) -> Pizza:
        pizza = self._pizza
        self.reset()
        return pizza

    def masa(self) -> None:
        '''
        El cliente selecciona el tipo de masa que quiere para su pizza
        '''
        while True:
            print("Seleccione el tipo de masa: \n- Masa tradicional\n- Masa integral\n- Masa sin gluten\n")
            opcion = input(">> ")
            if opcion in ["Masa tradicional", "Masa integral", "Masa sin gluten"]: 
                self._pizza.agregar(opcion)
                break
            else:
                print("Opción no valida\n")

    def salsa(self) -> None:
        '''
        El cliente selecciona el tipo de salsa que quiere para su pizza
        '''
        while True:
            print("Seleccione el tipo de salsa: \n- Salsa de tomate\n- Salsa barbacoa\n- Salsa carbonara\n")
            opcion = input(">> ")
            if opcion in ["Salsa de tomate", "Salsa barbacoa", "Salsa carbonara"]:
                self._pizza.agregar(opcion)
                break
            else:
                print("Opción no valida\n")

    def ingredientes(self) -> None:
        '''
        El cliente selecciona los ingredientes que quiere para su pizza, aunque también le damos una recomendación
        '''
        # Primero hacemos una recomendación basada en las opciones seleccionadas hasta ahora.
        if self._pizza.partes[0] == "Masa tradicional" and self._pizza.partes[1] == "Salsa de tomate":
            print("Le recomendamos agregar jamón y queso")
        elif self._pizza.partes[0] == "Masa integral" and self._pizza.partes[1] == "Salsa barbacoa":
            print("Le recomendamos agregar bacon y cebolla")
        elif self._pizza.partes[0] == "Masa sin gluten" and self._pizza.partes[1] == "Salsa carbonara":
            print("Le recomendamos agregar piña y carne picada")
        else:
            print("No hay recomendaciones de ingredientes")
        # Luego le pedimos que seleccione los ingredientes.
        while True:
            print("Seleccione los ingredientes separados por comas: \n- Jamon\n- Queso\n- Bacon\n- Cebolla\n- Pimiento\n- Piña\n- Carne picada\n- Pollo\n- Atun\n- Tomate\n- Aceitunas\n- Maiz\n- Champiñones\n- Anchoas\n- Salami\n- Pimiento picante\n- Rucula\n- Salsa barbacoa\n- Salsa carbonara\n")
            opciones = input(">> ").split(", ")
            no_validas = []
            for opcion in opciones:
                if opcion not in ["Jamon", "Queso", "Bacon", "Cebolla", "Pimiento", "Piña", "Carne picada", "Pollo", "Atun", "Tomate", "Aceitunas", "Maiz", "Champiñones", "Anchoas", "Salami", "Pimiento picante", "Rucula", "Salsa barbacoa", "Salsa carbonara"]:
                    no_validas.append(opcion)
                else:
                    pass
            if len(no_validas) == 0:
                self._pizza.agregar(opciones)
                break
            else:
                print("Hay alguna opción no válida, vuelva a intentarlo\n")

    def coccion(self) -> None:
        '''
        El cliente selecciona el tipo de cocción que quiere para su pizza
        '''
        while True:
            print("Seleccione el tipo de cocción: \n- Horno de leña\n- Horno electrico\n- Horno de gas\n")
            opcion = input(">> ")
            if opcion in ["Horno de leña", "Horno electrico", "Horno de gas"]:
                self._pizza.agregar(opcion)
                break
            else:
                print("Opción no valida\n")

    def presentacion(self) -> None:
        '''
        El cliente selecciona el tipo de presentación que quiere para su pizza
        '''
        while True:
            print("Seleccione el tipo de presentación: \n- Pizza entera\n- Pizza por raciones\n")
            opcion = input(">> ")
            if opcion in ["Pizza entera", "Pizza por raciones"]:
                self._pizza.agregar(opcion)
                break
            else:
                print("Opción no valida\n")

    def maridajes(self) -> None:
        '''
        El cliente selecciona el tipo de maridaje que quiere para su pizza, aunque también le damos una recomendación
        '''
        # Primero hacemos una recomendación basada en las opciones seleccionadas hasta ahora.
        if self._pizza.partes[0] == "Masa tradicional" and self._pizza.partes[1] == "Salsa de tomate" and self._pizza.partes[2] == ["Jamon", "Queso"]:
            print("Maridaje recomendado: Vino tinto")
        elif self._pizza.partes[0] == "Masa integral" and self._pizza.partes[1] == "Salsa barbacoa" and self._pizza.partes[2] == ["Bacon", "Cebolla"]:
            print("Maridaje recomendado: Vino blanco") 
        elif self._pizza.partes[0] == "Masa sin gluten" and self._pizza.partes[1] == "Salsa carbonara" and self._pizza.partes[2] == ["Piña", "Carne picada"]: 
            print("Maridaje recomendado: Cerveza sin gluten")
        else:
            print("No hay maridaje recomendado")
        # Luego le pedimos que seleccione los maridajes.
        while True:
            print("Seleccione un maridajes para acompañar: \n- Vino tinto\n- Vino blanco\n- Cerveza\n- Cerveza sin gluten\n- Refresco\n- Agua\n- None\n")
            opcion = input(">> ")
            if opcion in ["Vino tinto", "Vino blanco", "Cerveza", "Cerveza sin gluten", "Refresco", "Agua", "None"]:
                self._pizza.agregar(opcion)
                break
            else:
                print("Opción no válida\n")

    def extras(self) -> None:
        '''
        El cliente selecciona si quier agregar algún ingrediente extra a la pizza
        '''
        while True:
            print("Seleccione los extras separados por comas: \n- Queso extra\n- Jamon extra\n- Bacon extra\n- Cebolla extra\n- Pimiento extra\n- Piña extra\n- Carne picada extra\n- Pollo extra\n- Atun extra\n- Tomate extra\n- Aceitunas extra\n- Maiz extra\n- Champiñones extra\n- Anchoas extra\n- Salami extra\n- Pimiento picante extra\n- Rucula extra\n- Salsa barbacoa extra\n- Salsa carbonara extra\n- None\n")
            opciones = input(">> ").split(", ")
            no_validas = []
            for opcion in opciones:
                if opcion not in ["Queso extra", "Jamon extra", "Bacon extra", "Cebolla extra", "Pimiento extra", "Piña extra", "Carne picada extra", "Pollo extra", "Atun extra", "Tomate extra", "Aceitunas extra", "Maiz extra", "Champiñones extra", "Anchoas extra", "Salami extra", "Pimiento picante extra", "Rucula extra", "Salsa barbacoa extra", "Salsa carbonara extra", "None"]:
                    no_validas.append(opcion)
                else:
                    pass
            if len(no_validas) == 0:
                self._pizza.agregar(opciones)
                break
            else:
                print("Hay alguna opción no válida, vuelva a intentarlo\n")
```

#### Archivo `pizza.py`
```
from typing import Any
import csv


class Pizza():

    def __init__(self) -> None:
        self.partes = []

    def agregar(self, parte: Any) -> None:
        '''
        Agregamos las elecciones del cliente a la pizza
        '''
        self.partes.append(parte)
    
    def guardar_csv(self):
        '''
        Guardamos la pizza generada por el cliente en un archivo csv
        '''
        with open("Patrones creacionales/Ejercicio 2/data/pizza_cliente.csv", "a", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(self.partes)
    
    def ultima_fila(self):
        '''
        Con este método obtenemos la última fila del archivo csv
        '''
        with open("Patrones creacionales/Ejercicio 2/data/pizza_cliente.csv", "r") as archivo:
            reader = csv.reader(archivo)
            for row in reader:
                last_row = row
            return last_row

    def visualizacion_csv(self) -> None:
        '''
        Leemos el archivo csv y mostramos la pizza creada por el cliente
        '''
        for element in self.ultima_fila():
            if '[' in element and ']' in element:
                element = element.replace('[', '')
                element = element.replace(']', '')
                element = element.replace("'", '')
            else:
                pass
            print(f"- {element}")

    def borrar_pizza(self):
        '''
        En caso de que el cliente no quiera la pizza que creó, borramos la última fila del archivo csv
        '''
        f = open('Patrones creacionales/Ejercicio 2/data/pizza_cliente.csv', "r+")
        lines = f.readlines()
        lines.pop()
        f = open('Patrones creacionales/Ejercicio 2/data/pizza_cliente.csv', "w+")
        f.writelines(lines)
```

#### Archivo `gui.py`
```
import tkinter as tk
from tkinter import ttk

def boton_salir(root, pagina):
    exit_button = ttk.Button(pagina, text="Salir", command=root.quit)
    exit_button.pack(pady=20)


def ir_a_pagina(pagina_actual, pagina_deseada):
    pagina_actual.pack_forget()
    pagina_deseada.pack()


def boton_atras(pagina, pagina_anterior):
    atras_btn = ttk.Button(pagina, text="Atrás",
                            command=lambda: ir_a_pagina(pagina, pagina_anterior))
    atras_btn.pack(pady=20)


def cambiar_color(checkbutton, seleccionado):
    if seleccionado:
        checkbutton.configure(foreground="white", background="green")
    else:
        checkbutton.configure(foreground="black", background="SystemButtonFace")



def crear_pagina_inicio(root):
    pagina_inicio = tk.Frame(root)
    bienvenido_lb = tk.Label(pagina_inicio, text="¡Bienvenido a la Pizzería\nDELIZIOSO!", font=("Brush Script MT", 40, "bold"))
    bienvenido_lb.pack(padx=20, pady=20)
    inicio_lb = tk.Label(pagina_inicio, text="Donde nos especializamos en personalizar pizzas")
    inicio_lb.pack(padx=20, pady=20)

    comenzar_btn = ttk.Button(pagina_inicio, text="Empieza a preparar tu pizza",
                              command=lambda: ir_a_pagina(pagina_inicio, crear_pagina_masa(root)))
    comenzar_btn.pack(pady=20)

    boton_salir(root, pagina_inicio)

    return pagina_inicio


def crear_pagina_masa(root, tipo_masa="Masa tradicional"):
    pagina_masa = tk.Frame(root)
    masa_lb = tk.Label(pagina_masa, text="Elige tu tipo de masa:")
    masa_lb.pack(padx=20, pady=20)

    opciones = [
        ("Masa tradicional", "Masa tradicional"),
        ("Masa integral", "Masa integral"),
        ("Masa sin gluten", "Masa sin gluten")
    ]

    masa_var = tk.StringVar()
    masa_var.set(tipo_masa)

    for text, masa in opciones:
        tk.Radiobutton(pagina_masa, text=text, variable=masa_var, value=masa).pack(anchor="w")

    siguiente_btn = ttk.Button(pagina_masa, text="Siguiente",
                             command=lambda: ir_a_pagina(pagina_masa, crear_pagina_salsa(root)))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_masa, crear_pagina_inicio(root))

    return pagina_masa


def crear_pagina_salsa(root, tipo_salsa="Salsa de tomate"):
    pagina_salsa = tk.Frame(root)
    salsa_lb = tk.Label(pagina_salsa, text="Selecciona tu salsa:")
    salsa_lb.pack(padx=20, pady=20)

    opciones = [
        ("Salsa de tomate", "Salsa de tomate"),
        ("Salsa barbacoa", "Salsa barbacoa"),
        ("Salsa carbonara", "Salsa carbonara")
    ]

    salsa_var = tk.StringVar()
    salsa_var.set(tipo_salsa)

    for text, salsa in opciones:
        tk.Radiobutton(pagina_salsa, text=text, variable=salsa_var, value=salsa).pack(anchor="w")

    siguiente_btn = ttk.Button(pagina_salsa, text="Siguiente",
                             command=lambda: ir_a_pagina(pagina_salsa, crear_pagina_ingredientes(root)))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_salsa, crear_pagina_masa(root))

    return pagina_salsa


def crear_pagina_ingredientes(root):
    pagina_ingredientes = tk.Frame(root)
    ingredientes_lb = tk.Label(pagina_ingredientes, text="Elige tus ingredientes:")
    ingredientes_lb.pack(padx=20, pady=20)

    opciones_ingredientes = [
        "Jamon",
        "Queso",
        "Bacon",
        "Cebolla",
        "Pimiento",
        "Piña",
        "Carne picada",
        "Pollo",
        "Atun",
        "Tomate",
        "Aceitunas",
        "Maiz",
        "Champiñones",
        "Anchoas",
        "Salami",
        "Pimiento picante",
        "Rucula",
        "Salsa barbacoa",
        "Salsa carbonara"
    ]

    ingredientes_vars = []
    for ingrediente in opciones_ingredientes:
        var = tk.BooleanVar()
        c = ttk.Checkbutton(pagina_ingredientes, text=ingrediente, variable=var)
        c.pack(anchor='w')
        ingredientes_vars.append((ingrediente, var))
        c.configure(command=lambda checkbutton=c, var=var: cambiar_color(checkbutton, var.get()))


    siguiente_btn = ttk.Button(pagina_ingredientes, text="Siguiente",
                             command=lambda: ir_a_pagina(pagina_ingredientes, crear_pagina_coccion(root)))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_ingredientes, crear_pagina_salsa(root))

    return pagina_ingredientes


def crear_pagina_coccion(root, tipo_coccion="Horno de leña"):
    pagina_coccion = tk.Frame(root)
    coccion_lb = tk.Label(pagina_coccion, text="Selecciona el método de cocción:")
    coccion_lb.pack(padx=20, pady=20)

    opciones = [
        ("Horno de leña", "Horno de leña"),
        ("Horno electrico", "Horno electrico"),
        ("Horno de gas", "Horno de gas")
    ]

    coccion_var = tk.StringVar()
    coccion_var.set(tipo_coccion)

    for text, coccion in opciones:
        tk.Radiobutton(pagina_coccion, text=text, variable=coccion_var, value=coccion).pack(anchor="w")

    siguiente_btn = ttk.Button(pagina_coccion, text="Siguiente",
                             command=lambda: ir_a_pagina(pagina_coccion, crear_pagina_presentacion(root)))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_coccion, crear_pagina_ingredientes(root))

    return pagina_coccion


def crear_pagina_presentacion(root, tipo_presentacion="Pizza entera"):
    pagina_presentacion = tk.Frame(root)
    presentacion_lb = tk.Label(pagina_presentacion, text="Elige la presentación de la pizza:")
    presentacion_lb.pack(padx=20, pady=20)

    opciones = [
        ("Pizza entera", "Pizza entera"),
        ("Pizza por raciones", "Pizza por raciones")
    ]

    presentacion_var = tk.StringVar()
    presentacion_var.set(tipo_presentacion)

    for text, presentacion in opciones:
        tk.Radiobutton(pagina_presentacion, text=text, variable=presentacion_var, value=presentacion).pack(anchor="w")

    siguiente_btn = ttk.Button(pagina_presentacion, text="Siguiente",
                             command=lambda: ir_a_pagina(pagina_presentacion, crear_pagina_maridaje(root)))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_presentacion, crear_pagina_coccion(root))

    return pagina_presentacion


def crear_pagina_maridaje(root, tipo_bebida="None"):
    pagina_maridaje = tk.Frame(root)
    maridaje_lb = tk.Label(pagina_maridaje, text="Selecciona tus bebidas:")
    maridaje_lb.pack(padx=20, pady=20)

    opciones = [
        ("Vino tinto", "Vino tinto"),
        ("Vino blanco", "Vino blanco"),
        ("Cerveza", "Cerveza"),
        ("Cerveza sin gluten", "Cerveza sin gluten"),
        ("Refresco", "Refresco"),
        ("Agua", "Agua"),
        ("None", "None")
    ]

    bebida_var = tk.StringVar()
    bebida_var.set(tipo_bebida)

    for text, bebida in opciones:
        tk.Radiobutton(pagina_maridaje, text=text, variable=bebida_var, value=bebida).pack(anchor="w")


    siguiente_btn = ttk.Button(pagina_maridaje, text="Siguiente",
                             command=lambda: ir_a_pagina(pagina_maridaje, crear_pagina_extras(root)))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_maridaje, crear_pagina_presentacion(root))

    return pagina_maridaje


def crear_pagina_extras(root):
    pagina_extras = tk.Frame(root)
    extras_lb = tk.Label(pagina_extras, text="Agrega extras a tu pizza:")
    extras_lb.pack(padx=20, pady=20)

    opciones_extras = [
        "Queso extra",
        "Bacon extra",
        "Cebolla extra",
        "Piña extra",
        "Carne picada extra",
        "Pollo extra",
        "Atun extra",
        "Tomate extra",
        "Aceitunas extra",
        "Maiz extra",
        "Champiñones extra",
        "Anchoas extra",
        "Salami extra",
        "Pimiento picante extra",
        "Rucula extra",
        "Salsa barbacoa extra",
        "Salsa carbonara extra"
    ]

    extras_vars = []
    for extra in opciones_extras:
        var = tk.BooleanVar()
        c = ttk.Checkbutton(pagina_extras, text=extra, variable=var)
        c.pack(anchor='w')
        extras_vars.append((extra, var))
        c.configure(command=lambda checkbutton=c, var=var: cambiar_color(checkbutton, var.get()))


    siguiente_btn = ttk.Button(pagina_extras, text="Siguiente",
                             command=lambda: ir_a_pagina(pagina_extras, crear_pagina_final(root)))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_extras, crear_pagina_maridaje(root))

    return pagina_extras


def crear_pagina_final(root):
    pagina_final = tk.Frame(root)
    final_lb = tk.Label(pagina_final, text="¡Gracias por personalizar tu pizza!")
    final_lb.pack(padx=20, pady=20)

    gusto_lb = tk.Label(pagina_final, text="¿Te gusta la pizza?")
    gusto_lb.pack(padx=20, pady=20)

    volver_btn = ttk.Button(pagina_final, text="No, comenzar de nuevo", 
                             command=lambda: ir_a_pagina(pagina_final, crear_pagina_masa(root)))
    volver_btn.pack(pady=20)

    siguiente_btn = ttk.Button(pagina_final, text="Sí, finalizar",
                             command=lambda: ir_a_pagina(pagina_final, crear_pagina_inicio(root)))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_final, crear_pagina_extras(root))

    return pagina_final
```

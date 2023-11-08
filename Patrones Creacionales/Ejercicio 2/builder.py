from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
import csv

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
        while True:
            print("Seleccione el tipo de masa: \n- Masa tradicional\n- Masa integral\n- Masa sin gluten\n")
            opcion = input(">> ")
            if opcion in ["Masa tradicional", "Masa integral", "Masa sin gluten"]:
                self._pizza.agregar(opcion)
                break
            else:
                print("Opción no valida")

    def salsa(self) -> None:
        while True:
            print("Seleccione el tipo de salsa: \n- Salsa de tomate\n- Salsa barbacoa\n- Salsa carbonara\n")
            opcion = input(">> ")
            if opcion in ["Salsa de tomate", "Salsa barbacoa", "Salsa carbonara"]:
                self._pizza.agregar(opcion)
                break
            else:
                print("Opción no valida")

    def ingredientes(self) -> None:
        while True:
            print("Seleccione los ingredientes separados por comas: \n- Jamón\n- Queso\n- Bacon\n- Cebolla\n- Pimiento\n- Piña\n- Carne picada\n- Pollo\n- Atún\n- Tomate\n- Aceitunas\n- Maíz\n- Champiñones\n- Anchoas\n- Salami\n- Pimiento picante\n- Rúcula\n- Salsa barbacoa\n- Salsa carbonara\n")
            opciones = input(">> ").split(",")
            validas = []
            for opcion in opciones:
                if opcion not in ["Jamón", "Queso", "Bacon", "Cebolla", "Pimiento", "Piña", "Carne picada", "Pollo", "Atún", "Tomate", "Aceitunas", "Maíz", "Champiñones", "Anchoas", "Salami", "Pimiento picante", "Rúcula", "Salsa barbacoa", "Salsa carbonara"]:
                    validas.append(opcion)
                else:
                    pass
            if len(validas) == 0:
                self._pizza.agregar(opciones)
                break
            else:
                print("Hay alguna opción no válida, vuelva a intentarlo")

    def coccion(self) -> None:
        while True:
            print("Seleccione el tipo de cocción: \n- Horno de leña\n- Horno eléctrico\n- Horno de gas\n")
            opcion = input(">> ")
            if opcion in ["Horno de leña", "Horno eléctrico", "Horno de gas"]:
                self._pizza.agregar(opcion)
                break
            else:
                print("Opción no valida")

    def presentacion(self) -> None:
        while True:
            print("Seleccione el tipo de presentación: \n- Pizza entera\n- Pizza por raciones\n")
            opcion = input(">> ")
            if opcion in ["Pizza entera", "Pizza por raciones"]:
                self._pizza.agregar(opcion)
                break
            else:
                print("Opción no valida")

    def maridajes(self) -> None:
        if self.masa == "Masa tradicional":
            print("Maridaje recomendado: Vino tinto")
        elif self.masa == "Masa integral":
            print("Maridaje recomendado: Vino blanco")
        elif self.masa == "Masa sin gluten":
            print("Maridaje recomendado: Cerveza sin gluten")
        else:
            pass

    def extras(self) -> None:
        while True:
            print("Seleccione los extras separados por comas: \n- Queso extra\n- Jamón extra\n- Bacon extra\n- Cebolla extra\n- Pimiento extra\n- Piña extra\n- Carne picada extra\n- Pollo extra\n- Atún extra\n- Tomate extra\n- Aceitunas extra\n- Maíz extra\n- Champiñones extra\n- Anchoas extra\n- Salami extra\n- Pimiento picante extra\n- Rúcula extra\n- Salsa barbacoa extra\n- Salsa carbonara extra\n- None")
            opciones = input(">> ").split(",")
            validas = []
            for opcion in opciones:
                if opcion not in ["Queso extra", "Jamón extra", "Bacon extra", "Cebolla extra", "Pimiento extra", "Piña extra", "Carne picada extra", "Pollo extra", "Atún extra", "Tomate extra", "Aceitunas extra", "Maíz extra", "Champiñones extra", "Anchoas extra", "Salami extra", "Pimiento picante extra", "Rúcula extra", "Salsa barbacoa extra", "Salsa carbonara extra", "None"]:
                    validas.append(opcion)
                else:
                    pass
            if len(validas) == 0:
                self._pizza.agregar(opciones)
                break
            else:
                print("Hay alguna opción no válida, vuelva a intentarlo")


class Pizza():

    def __init__(self) -> None:
        self.partes = []

    def agregar(self, parte: Any) -> None:
        self.partes.append(parte)

    def escribir_partes(self) -> None:
        for element in self.partes:
            if type(element) == list:
                for el in element:
                    print(f"- {el}")
            else:
                print(f"- {element}")
    
    def guardar_csv(self):
        with open("Patrones creacionales/Ejercicio 2/data/pizza_cliente.csv", "a", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(self.partes)

class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def construir_min(self) -> None:
        self.builder.masa()
        self.builder.salsa()
        self.builder.ingredientes()
        self.builder.coccion()

    def construir_completo(self) -> None:
        self.builder.masa()
        self.builder.salsa()
        self.builder.ingredientes()
        self.builder.coccion()
        self.builder.presentacion()
        self.builder.maridajes()
        self.builder.extras()

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


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



class ConcreteBuilder1(Builder):

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
                self._pizza.add(opcion)
                break
            else:
                print("Opción no valida")

    def salsa(self) -> None:
        while True:
            print("Seleccione el tipo de salsa: \n- Salsa de tomate\n- Salsa barbacoa\n- Salsa carbonara\n")
            opcion = input(">> ")
            if opcion in ["Salsa de tomate", "Salsa barbacoa", "Salsa carbonara"]:
                self._pizza.add(opcion)
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
                self._pizza.add(opciones)
                break
            else:
                print("Hay alguna opción no válida, vuelva a intentarlo")

    def coccion(self) -> None:
        while True:
            print("Seleccione el tipo de cocción: \n- Horno de leña\n- Horno eléctrico\n- Horno de gas\n")
            opcion = input(">> ")
            if opcion in ["Horno de leña", "Horno eléctrico", "Horno de gas"]:
                self._pizza.add(opcion)
                break
            else:
                print("Opción no valida")

    def presentacion(self) -> None:
        while True:
            print("Seleccione el tipo de presentación: \n- Pizza entera\n- Pizza por raciones\n")
            opcion = input(">> ")
            if opcion in ["Pizza entera", "Pizza por raciones"]:
                self._pizza.add(opcion)
                break
            else:
                print("Opción no valida")

    def maridajes(self) -> None:
        #TODO
        pass

    def extras(self) -> None:
        while True:
            print("Seleccione los extras separados por comas: \n- Queso extra\n- Jamón extra\n- Bacon extra\n- Cebolla extra\n- Pimiento extra\n- Piña extra\n- Carne picada extra\n- Pollo extra\n- Atún extra\n- Tomate extra\n- Aceitunas extra\n- Maíz extra\n- Champiñones extra\n- Anchoas extra\n- Salami extra\n- Pimiento picante extra\n- Rúcula extra\n- Salsa barbacoa extra\n- Salsa carbonara extra\n")
            opciones = input(">> ").split(",")
            validas = []
            for opcion in opciones:
                if opcion not in ["Queso extra", "Jamón extra", "Bacon extra", "Cebolla extra", "Pimiento extra", "Piña extra", "Carne picada extra", "Pollo extra", "Atún extra", "Tomate extra", "Aceitunas extra", "Maíz extra", "Champiñones extra", "Anchoas extra", "Salami extra", "Pimiento picante extra", "Rúcula extra", "Salsa barbacoa extra", "Salsa carbonara extra"]:
                    validas.append(opcion)
                else:
                    pass
            if len(validas) == 0:
                self._pizza.add(opciones)
                break
            else:
                print("Hay alguna opción no válida, vuelva a intentarlo")


class Product1():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
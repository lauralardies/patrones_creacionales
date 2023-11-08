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
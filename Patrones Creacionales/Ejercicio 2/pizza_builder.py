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
        # Primero hacemos una recomendación basada en las opciones seleccionadas hasta ahora.
        if self.masa == "Masa tradicional" and self.salsa == "Salsa de tomate":
            print("Le recomendamos agregar jamón y queso")
        elif self.masa == "Masa integral" and self.salsa == "Salsa barbacoa":
            print("Le recomendamos agregar bacon y cebolla")
        elif self.masa == "Masa sin gluten" and self.salsa == "Salsa carbonara":
            print("Le recomendamos agregar piña y carne picada")
        else:
            print("No hay recomendaciones de ingredientes")
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
                print("Hay alguna opción no válida, vuelva a intentarlo")

    def coccion(self) -> None:
        while True:
            print("Seleccione el tipo de cocción: \n- Horno de leña\n- Horno electrico\n- Horno de gas\n")
            opcion = input(">> ")
            if opcion in ["Horno de leña", "Horno electrico", "Horno de gas"]:
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
        if self.masa == "Masa tradicional" and self.salsa == "Salsa de tomate" and self.ingredientes == ["Jamon", "Queso"]:
            print("Maridaje recomendado: Vino tinto")
        elif self.masa == "Masa integral" and self.salsa == "Salsa barbacoa" and self.ingredientes == ["Bacon", "Cebolla"]:
            print("Maridaje recomendado: Vino blanco") 
        elif self.masa == "Masa sin gluten" and self.salsa == "Salsa carbonara" and self.ingredientes == ["Piña", "Carne picada"]: 
            print("Maridaje recomendado: Cerveza sin gluten")
        else:
            print("No hay maridaje recomendado")
        while True:
            print("Seleccione los maridajes separados por comas: \n- Vino tinto\n- Vino blanco\n- Cerveza\n- Cerveza sin gluten\n- Refresco\n- Agua\n- None\n")
            opciones = input(">> ").split(", ")
            no_validas = []
            for opcion in opciones:
                if opcion not in ["Vino tinto", "Vino blanco", "Cerveza", "Cerveza sin gluten", "Refresco", "Agua", "None"]:
                    no_validas.append(opcion)
                else:
                    pass
            if len(no_validas) == 0:
                self._pizza.agregar(opciones)
                break
            else:
                print("Hay alguna opción no válida, vuelva a intentarlo")

    def extras(self) -> None:
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
                print("Hay alguna opción no válida, vuelva a intentarlo")
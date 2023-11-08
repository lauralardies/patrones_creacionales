from director import Director
from pizza_builder import PizzaBuilder

if __name__ == "__main__":

    director = Director()
    builder = PizzaBuilder()
    director.builder = builder

    print("Crea tu pizza: ")
    director.construir_completo()
    builder.pizza.guardar_csv()
from builder import PizzaBuilder, Director

if __name__ == "__main__":

    director = Director()
    builder = PizzaBuilder()
    director.builder = builder

    print("Crea tu pizza: ")
    director.construir_completo()
    builder.pizza.guardar_csv()
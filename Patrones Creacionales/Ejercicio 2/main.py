from director import Director
from pizza_builder import PizzaBuilder
from config import limpiar_pantalla


def main():
    '''
    Desde esta función, el cliente podrá acceder a los servicios de la pizzeria
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
        if respuesta.capitalize() == 'N': # Si no le gusta, volvemos a empezar
            builder.pizza.borrar_pizza()
            print('Empecemos de nuevo')
            input('Presiona cualquier tecla para continuar...')
        else: # Si le gusta, guardamos la pizza y terminamos
            print('¡Gracias por tu compra!')
            break
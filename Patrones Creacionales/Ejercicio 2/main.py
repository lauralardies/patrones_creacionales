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

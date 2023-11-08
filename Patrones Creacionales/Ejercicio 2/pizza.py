from typing import Any
import csv


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
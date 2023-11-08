import csv

def guardar_pizza(pizza):
    with open("pizza.csv", "a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(pizza)

def leer_csv(nombre_archivo):
    pizzas = []
    with open(nombre_archivo, mode="r") as archivo:
        reader = csv.reader(archivo)
        for linea in reader:
            pizza = []
            for elemento in linea:
                if '[' in elemento and ']' in elemento:
                    pizza.append(elemento[1:-1].split(", "))
                else:
                    pizza.append(elemento)
            pizzas.append(pizza)
    return pizzas

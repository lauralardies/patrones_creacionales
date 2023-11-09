import tkinter as tk
from gui import crear_pagina_inicio, crear_pagina_masa, crear_pagina_salsa, crear_pagina_ingredientes, crear_pagina_coccion, crear_pagina_presentacion, crear_pagina_maridaje, crear_pagina_extras, crear_pagina_final
from PIL import Image, ImageTk


def main():

    root = tk.Tk()
    root.title("Personaliza tu pizza")
    root.geometry("1100x600")

    image = Image.open("Patrones Creacionales/Ejercicio 2/img/pizza_index.jpg")  # Cambia la ruta por la ubicación de tu imagen
    background_image = ImageTk.PhotoImage(image)

    # Mostrar la imagen en un widget de etiqueta
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Ajusta la posición y el tamaño de la imagen

    pagina_inicio = crear_pagina_inicio(root)
    pagina_masa = crear_pagina_masa(root)
    pagina_salsa = crear_pagina_salsa(root)
    pagina_ingredientes = crear_pagina_ingredientes(root)
    pagina_coccion = crear_pagina_coccion(root)
    pagina_presentacion = crear_pagina_presentacion(root)
    pagina_maridaje = crear_pagina_maridaje(root)
    pagina_extras = crear_pagina_extras(root)
    pagina_final = crear_pagina_final(root)

    pagina_inicio.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
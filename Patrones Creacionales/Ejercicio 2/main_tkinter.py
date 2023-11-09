import tkinter as tk
from gui import crear_pagina_inicio, crear_pagina_masa, crear_pagina_salsa, crear_pagina_ingredientes, crear_pagina_coccion, crear_pagina_presentacion, crear_pagina_maridaje, crear_pagina_extras, crear_pagina_final


def main():

    root = tk.Tk()
    root.title("Personaliza tu pizza")

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
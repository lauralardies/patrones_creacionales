import tkinter as tk
from tkinter import ttk



def boton_salir(pagina):
    exit_button = ttk.Button(pagina, text="Salir", command=root.quit)
    exit_button.pack(pady=20)

def ir_siguiente_pagina(pagina_actual, siguiente_pagina):
    pagina_actual.pack_forget()
    siguiente_pagina.pack()

def ir_pagina_anterior(pagina_actual, pagina_anterior):
    pagina_actual.pack_forget()
    pagina_anterior.pack()

def boton_atras(pagina, pagina_anterior):
    atras_btn = ttk.Button(pagina, text="Atrás",
                            command=lambda: ir_pagina_anterior(pagina, pagina_anterior))
    atras_btn.pack(pady=20)

def pagina_inicio(root):
    pagina_inicio = tk.Frame(root)
    inicio_lb = tk.Label(pagina_inicio, text="¡Bienvenido a la personalización de pizza!")
    inicio_lb.pack(padx=20, pady=20)

    comenzar_btn = ttk.Button(pagina_inicio, text="Empieza a preparar tu pizza",
                              command=lambda: ir_siguiente_pagina(pagina_inicio, pagina_masa))
    comenzar_btn.pack(pady=20)

    boton_salir(pagina_inicio)

    return pagina_inicio

def pagina_masa(root):
    pagina_masa = tk.Frame(root)
    masa_lb = tk.Label(pagina_masa, text="Elige tu tipo de masa:")
    masa_lb.pack(padx=20, pady=20)

    # Aquí puedes agregar elementos como botones de radio para los tipos de masa

    siguiente_btn = ttk.Button(pagina_masa, text="Siguiente",
                             command=lambda: ir_siguiente_pagina(pagina_masa, pagina_salsa))
    siguiente_btn.pack(pady=20)

    return pagina_masa

def pagina_salsa(root):
    pagina_salsa = tk.Frame(root)
    salsa_lb = tk.Label(pagina_salsa, text="Selecciona tu salsa:")
    salsa_lb.pack(padx=20, pady=20)

    # Aquí puedes agregar elementos como botones de radio para las salsas

    siguiente_btn = ttk.Button(pagina_salsa, text="Siguiente",
                             command=lambda: ir_siguiente_pagina(pagina_salsa, pagina_ingredientes))
    siguiente_btn.pack(pady=20)

    return pagina_salsa

def pagina_ingredientes(root):
    pagina_ingredientes = tk.Frame(root)
    ingredientes_lb = tk.Label(pagina_ingredientes, text="Elige tus ingredientes:")
    ingredientes_lb.pack(padx=20, pady=20)

    # Aquí puedes agregar elementos como casillas de verificación para los ingredientes

    siguiente_btn = ttk.Button(pagina_ingredientes, text="Siguiente",
                             command=lambda: ir_siguiente_pagina(pagina_ingredientes, pagina_coccion))
    siguiente_btn.pack(pady=20)

    return pagina_ingredientes

def pagina_coccion(root):
    pagina_coccion = tk.Frame(root)
    coccion_lb = tk.Label(pagina_coccion, text="Selecciona el método de cocción:")
    coccion_lb.pack(padx=20, pady=20)

    # Aquí puedes agregar elementos como botones de radio para los métodos de cocción

    siguiente_btn = ttk.Button(pagina_coccion, text="Siguiente",
                             command=lambda: ir_siguiente_pagina(pagina_coccion, pagina_presentacion))
    siguiente_btn.pack(pady=20)

    return pagina_coccion

def pagina_presentacion(root):
    pagina_presentacion = tk.Frame(root)
    presentacion_lb = tk.Label(pagina_presentacion, text="Elige la presentación de la pizza:")
    presentacion_lb.pack(padx=20, pady=20)

    # Aquí puedes agregar elementos como botones de radio para las opciones de presentación

    siguiente_btn = ttk.Button(pagina_presentacion, text="Siguiente",
                             command=lambda: ir_siguiente_pagina(pagina_presentacion, pagina_maridaje))
    siguiente_btn.pack(pady=20)

    return pagina_presentacion

def pagina_maridaje(root):
    pagina_maridaje = tk.Frame(root)
    maridaje_lb = tk.Label(pagina_maridaje, text="Selecciona tus bebidas:")
    maridaje_lb.pack(padx=20, pady=20)

    # Aquí puedes agregar elementos como casillas de verificación para las bebidas

    siguiente_btn = ttk.Button(pagina_maridaje, text="Siguiente",
                             command=lambda: ir_siguiente_pagina(pagina_maridaje, pagina_extras))
    siguiente_btn.pack(pady=20)

    return pagina_maridaje

def pagina_extras(root):
    pagina_extras = tk.Frame(root)
    extras_lb = tk.Label(pagina_extras, text="Agrega extras a tu pizza:")
    extras_lb.pack(padx=20, pady=20)

    # Aquí puedes agregar elementos como casillas de verificación para los extras

    siguiente_btn = ttk.Button(pagina_extras, text="Finalizar",
                             command=lambda: ir_siguiente_pagina(pagina_extras, pagina_inicio))
    siguiente_btn.pack(pady=20)

    return pagina_extras

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Personaliza tu pizza")

    pagina_inicio = pagina_inicio(root)
    pagina_masa = pagina_masa(root)
    pagina_salsa = pagina_salsa(root)
    pagina_ingredientes = pagina_ingredientes(root)
    pagina_coccion = pagina_coccion(root)
    pagina_presentacion = pagina_presentacion(root)
    pagina_maridaje = pagina_maridaje(root)
    pagina_extras = pagina_extras(root)

    pagina_inicio.pack()

    root.mainloop()
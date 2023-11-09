import tkinter as tk
from tkinter import ttk

def boton_salir(root, pagina):
    exit_button = ttk.Button(pagina, text="Salir", command=root.quit)
    exit_button.pack(pady=20)


def ir_a_pagina(pagina_actual, pagina_deseada):
    pagina_actual.pack_forget()
    pagina_deseada.pack()


def boton_atras(pagina, pagina_anterior):
    atras_btn = ttk.Button(pagina, text="Atrás",
                            command=lambda: ir_a_pagina(pagina, pagina_anterior))
    atras_btn.pack(pady=20)


def cambiar_color(checkbutton, seleccionado):
    if seleccionado:
        checkbutton.configure(foreground="white", background="green")
    else:
        checkbutton.configure(foreground="black", background="SystemButtonFace")



def crear_pagina_inicio(root):
    pagina_inicio = tk.Frame(root)
    bienvenido_lb = tk.Label(pagina_inicio, text="¡Bienvenido a la Pizzería\nDELIZIOSO!", font=("Brush Script MT", 40, "bold"))
    bienvenido_lb.pack(padx=20, pady=20)
    inicio_lb = tk.Label(pagina_inicio, text="Donde nos especializamos en personalizar pizzas")
    inicio_lb.pack(padx=20, pady=20)

    comenzar_btn = ttk.Button(pagina_inicio, text="Empieza a preparar tu pizza",
                              command=lambda: ir_a_pagina(pagina_inicio, crear_pagina_masa(root)))
    comenzar_btn.pack(pady=20)

    boton_salir(root, pagina_inicio)

    return pagina_inicio


def crear_pagina_masa(root, tipo_masa="Masa tradicional"):
    pagina_masa = tk.Frame(root)
    masa_lb = tk.Label(pagina_masa, text="Elige tu tipo de masa:")
    masa_lb.pack(padx=20, pady=20)

    opciones = [
        ("Masa tradicional", "Masa tradicional"),
        ("Masa integral", "Masa integral"),
        ("Masa sin gluten", "Masa sin gluten")
    ]

    masa_var = tk.StringVar()
    masa_var.set(tipo_masa)

    for text, masa in opciones:
        tk.Radiobutton(pagina_masa, text=text, variable=masa_var, value=masa).pack(anchor="w")

    siguiente_btn = ttk.Button(pagina_masa, text="Siguiente",
                             command=lambda: ir_a_pagina(pagina_masa, crear_pagina_salsa(root)))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_masa, crear_pagina_inicio(root))

    return pagina_masa


def crear_pagina_salsa(root, tipo_salsa="Salsa de tomate"):
    pagina_salsa = tk.Frame(root)
    salsa_lb = tk.Label(pagina_salsa, text="Selecciona tu salsa:")
    salsa_lb.pack(padx=20, pady=20)

    opciones = [
        ("Salsa de tomate", "Salsa de tomate"),
        ("Salsa barbacoa", "Salsa barbacoa"),
        ("Salsa carbonara", "Salsa carbonara")
    ]

    salsa_var = tk.StringVar()
    salsa_var.set(tipo_salsa)

    for text, salsa in opciones:
        tk.Radiobutton(pagina_salsa, text=text, variable=salsa_var, value=salsa).pack(anchor="w")

    siguiente_btn = ttk.Button(pagina_salsa, text="Siguiente",
                             command=lambda: ir_a_pagina(pagina_salsa, crear_pagina_ingredientes(root)))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_salsa, crear_pagina_masa(root))

    return pagina_salsa


def crear_pagina_ingredientes(root):
    pagina_ingredientes = tk.Frame(root)
    ingredientes_lb = tk.Label(pagina_ingredientes, text="Elige tus ingredientes:")
    ingredientes_lb.pack(padx=20, pady=20)

    opciones_ingredientes = [
        "Jamon",
        "Queso",
        "Bacon",
        "Cebolla",
        "Pimiento",
        "Piña",
        "Carne picada",
        "Pollo",
        "Atun",
        "Tomate",
        "Aceitunas",
        "Maiz",
        "Champiñones",
        "Anchoas",
        "Salami",
        "Pimiento picante",
        "Rucula",
        "Salsa barbacoa",
        "Salsa carbonara"
    ]

    ingredientes_vars = []
    for ingrediente in opciones_ingredientes:
        var = tk.BooleanVar()
        c = ttk.Checkbutton(pagina_ingredientes, text=ingrediente, variable=var)
        c.pack(anchor='w')
        ingredientes_vars.append((ingrediente, var))
        c.configure(command=lambda checkbutton=c, var=var: cambiar_color(checkbutton, var.get()))


    siguiente_btn = ttk.Button(pagina_ingredientes, text="Siguiente",
                             command=lambda: ir_a_pagina(pagina_ingredientes, crear_pagina_coccion(root)))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_ingredientes, crear_pagina_salsa(root))

    return pagina_ingredientes


def crear_pagina_coccion(root, tipo_coccion="Horno de leña"):
    pagina_coccion = tk.Frame(root)
    coccion_lb = tk.Label(pagina_coccion, text="Selecciona el método de cocción:")
    coccion_lb.pack(padx=20, pady=20)

    opciones = [
        ("Horno de leña", "Horno de leña"),
        ("Horno electrico", "Horno electrico"),
        ("Horno de gas", "Horno de gas")
    ]

    coccion_var = tk.StringVar()
    coccion_var.set(tipo_coccion)

    for text, coccion in opciones:
        tk.Radiobutton(pagina_coccion, text=text, variable=coccion_var, value=coccion).pack(anchor="w")

    siguiente_btn = ttk.Button(pagina_coccion, text="Siguiente",
                             command=lambda: ir_a_pagina(pagina_coccion, crear_pagina_presentacion(root)))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_coccion, crear_pagina_ingredientes(root))

    return pagina_coccion


def crear_pagina_presentacion(root, tipo_presentacion="Pizza entera"):
    pagina_presentacion = tk.Frame(root)
    presentacion_lb = tk.Label(pagina_presentacion, text="Elige la presentación de la pizza:")
    presentacion_lb.pack(padx=20, pady=20)

    opciones = [
        ("Pizza entera", "Pizza entera"),
        ("Pizza por raciones", "Pizza por raciones")
    ]

    presentacion_var = tk.StringVar()
    presentacion_var.set(tipo_presentacion)

    for text, presentacion in opciones:
        tk.Radiobutton(pagina_presentacion, text=text, variable=presentacion_var, value=presentacion).pack(anchor="w")

    siguiente_btn = ttk.Button(pagina_presentacion, text="Siguiente",
                             command=lambda: ir_a_pagina(pagina_presentacion, crear_pagina_maridaje(root)))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_presentacion, crear_pagina_coccion(root))

    return pagina_presentacion


def crear_pagina_maridaje(root, tipo_bebida="None"):
    pagina_maridaje = tk.Frame(root)
    maridaje_lb = tk.Label(pagina_maridaje, text="Selecciona tus bebidas:")
    maridaje_lb.pack(padx=20, pady=20)

    opciones = [
        ("Vino tinto", "Vino tinto"),
        ("Vino blanco", "Vino blanco"),
        ("Cerveza", "Cerveza"),
        ("Cerveza sin gluten", "Cerveza sin gluten"),
        ("Refresco", "Refresco"),
        ("Agua", "Agua"),
        ("None", "None")
    ]

    bebida_var = tk.StringVar()
    bebida_var.set(tipo_bebida)

    for text, bebida in opciones:
        tk.Radiobutton(pagina_maridaje, text=text, variable=bebida_var, value=bebida).pack(anchor="w")


    siguiente_btn = ttk.Button(pagina_maridaje, text="Siguiente",
                             command=lambda: ir_a_pagina(pagina_maridaje, crear_pagina_extras(root)))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_maridaje, crear_pagina_presentacion(root))

    return pagina_maridaje


def crear_pagina_extras(root):
    pagina_extras = tk.Frame(root)
    extras_lb = tk.Label(pagina_extras, text="Agrega extras a tu pizza:")
    extras_lb.pack(padx=20, pady=20)

    opciones_extras = [
        "Queso extra",
        "Bacon extra",
        "Cebolla extra",
        "Piña extra",
        "Carne picada extra",
        "Pollo extra",
        "Atun extra",
        "Tomate extra",
        "Aceitunas extra",
        "Maiz extra",
        "Champiñones extra",
        "Anchoas extra",
        "Salami extra",
        "Pimiento picante extra",
        "Rucula extra",
        "Salsa barbacoa extra",
        "Salsa carbonara extra"
    ]

    extras_vars = []
    for extra in opciones_extras:
        var = tk.BooleanVar()
        c = ttk.Checkbutton(pagina_extras, text=extra, variable=var)
        c.pack(anchor='w')
        extras_vars.append((extra, var))
        c.configure(command=lambda checkbutton=c, var=var: cambiar_color(checkbutton, var.get()))


    siguiente_btn = ttk.Button(pagina_extras, text="Siguiente",
                             command=lambda: ir_a_pagina(pagina_extras, crear_pagina_final(root)))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_extras, crear_pagina_maridaje(root))

    return pagina_extras


def crear_pagina_final(root):
    pagina_final = tk.Frame(root)
    final_lb = tk.Label(pagina_final, text="¡Gracias por personalizar tu pizza!")
    final_lb.pack(padx=20, pady=20)

    gusto_lb = tk.Label(pagina_final, text="¿Te gusta la pizza?")
    gusto_lb.pack(padx=20, pady=20)

    volver_btn = ttk.Button(pagina_final, text="No, comenzar de nuevo", 
                             command=lambda: ir_a_pagina(pagina_final, crear_pagina_masa(root)))
    volver_btn.pack(pady=20)

    siguiente_btn = ttk.Button(pagina_final, text="Sí, finalizar",
                             command=lambda: ir_a_pagina(pagina_final, crear_pagina_inicio(root)))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_final, crear_pagina_extras(root))

    return pagina_final
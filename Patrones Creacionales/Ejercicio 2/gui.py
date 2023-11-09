import tkinter as tk
from tkinter import ttk



def boton_salir(pagina):
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


def pagina_inicio(root):
    pagina_inicio = tk.Frame(root)
    inicio_lb = tk.Label(pagina_inicio, text="¡Bienvenido a la personalización de pizza!")
    inicio_lb.pack(padx=20, pady=20)

    comenzar_btn = ttk.Button(pagina_inicio, text="Empieza a preparar tu pizza",
                              command=lambda: ir_a_pagina(pagina_inicio, pagina_masa))
    comenzar_btn.pack(pady=20)

    boton_salir(pagina_inicio)

    return pagina_inicio


def pagina_masa(root, tipo_masa="Masa tradicional"):
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
                             command=lambda: ir_a_pagina(pagina_masa, pagina_salsa))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_masa, pagina_inicio)

    return pagina_masa


def pagina_salsa(root, tipo_salsa="Salsa de tomate"):
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
                             command=lambda: ir_a_pagina(pagina_salsa, pagina_ingredientes))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_salsa, pagina_masa)

    return pagina_salsa


def pagina_ingredientes(root):
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
                             command=lambda: ir_a_pagina(pagina_ingredientes, pagina_coccion))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_ingredientes, pagina_salsa)

    return pagina_ingredientes


def pagina_coccion(root, tipo_coccion="Horno de leña"):
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
                             command=lambda: ir_a_pagina(pagina_coccion, pagina_presentacion))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_coccion, pagina_ingredientes)

    return pagina_coccion


def pagina_presentacion(root, tipo_presentacion="Pizza entera"):
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
                             command=lambda: ir_a_pagina(pagina_presentacion, pagina_maridaje))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_presentacion, pagina_coccion)

    return pagina_presentacion


def pagina_maridaje(root, tipo_bebida="None"):
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
                             command=lambda: ir_a_pagina(pagina_maridaje, pagina_extras))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_maridaje, pagina_presentacion)

    return pagina_maridaje


def pagina_extras(root):
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
                             command=lambda: ir_a_pagina(pagina_extras, pagina_final))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_extras, pagina_maridaje)

    return pagina_extras


def pagina_final(root):
    pagina_final = tk.Frame(root)
    final_lb = tk.Label(pagina_final, text="¡Gracias por personalizar tu pizza!")
    final_lb.pack(padx=20, pady=20)

    # Aquí puedes agregar elementos como etiquetas para mostrar el resumen de la pizza

    gusto_lb = tk.Label(pagina_final, text="¿Te gusta la pizza?")
    gusto_lb.pack(padx=20, pady=20)

    volver_btn = ttk.Button(pagina_final, text="No, comenzar de nuevo", 
                             command=lambda: ir_a_pagina(pagina_final, pagina_masa))
    volver_btn.pack(pady=20)

    siguiente_btn = ttk.Button(pagina_final, text="Sí, finalizar",
                             command=lambda: ir_a_pagina(pagina_final, pagina_inicio))
    siguiente_btn.pack(pady=20)

    boton_atras(pagina_final, pagina_extras)

    return pagina_final

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
    pagina_final = pagina_final(root)

    pagina_inicio.pack()

    root.mainloop()
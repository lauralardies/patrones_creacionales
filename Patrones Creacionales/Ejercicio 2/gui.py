import tkinter as tk

root = tk.Tk()

root.geometry("1100x700")
root.title("Pizzería DELIZIOSO")

opciones_frame = tk.Frame(root, bg='#c2c2c2')

inicio_btn = tk.Button(opciones_frame, text="Inicio", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
inicio_btn.place(x=30, y=100)
inicio_indicador = tk.Label(opciones_frame, text="", bg='#9b9b9b', font=('Arial', 12, 'bold'))
inicio_indicador.place(x=15, y=100, width=10, height=50)


paso1_btn = tk.Button(opciones_frame, text="Paso 1", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
paso1_btn.place(x=30, y=155)
paso1_indicador = tk.Label(opciones_frame, text="", bg='#9b9b9b', font=('Arial', 12, 'bold'))
paso1_indicador.place(x=15, y=155, width=10, height=50)


paso2_btn = tk.Button(opciones_frame, text="Paso 2", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
paso2_btn.place(x=30, y=210)
paso2_indicador = tk.Label(opciones_frame, text="", bg='#9b9b9b', font=('Arial', 12, 'bold'))
paso2_indicador.place(x=15, y=210, width=10, height=50)


paso3_btn = tk.Button(opciones_frame, text="Paso 3", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
paso3_btn.place(x=30, y=265)
paso3_indicador = tk.Label(opciones_frame, text="", bg='#9b9b9b', font=('Arial', 12, 'bold'))
paso3_indicador.place(x=15, y=265, width=10, height=50)


paso4_btn = tk.Button(opciones_frame, text="Paso 4", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
paso4_btn.place(x=30, y=320)
paso4_indicador = tk.Label(opciones_frame, text="", bg='#9b9b9b', font=('Arial', 12, 'bold'))
paso4_indicador.place(x=15, y=320, width=10, height=50)


paso5_btn = tk.Button(opciones_frame, text="Paso 5", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
paso5_btn.place(x=30, y=375)
paso5_indicador = tk.Label(opciones_frame, text="", bg='#9b9b9b', font=('Arial', 12, 'bold'))
paso5_indicador.place(x=15, y=375, width=10, height=50)


paso6_btn = tk.Button(opciones_frame, text="Paso 6", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
paso6_btn.place(x=30, y=430)
paso6_indicador = tk.Label(opciones_frame, text="", bg='#9b9b9b', font=('Arial', 12, 'bold'))
paso6_indicador.place(x=15, y=430, width=10, height=50)


paso7_btn = tk.Button(opciones_frame, text="Paso 7", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
paso7_btn.place(x=30, y=485)
paso7_indicador = tk.Label(opciones_frame, text="", bg='#9b9b9b', font=('Arial', 12, 'bold'))
paso7_indicador.place(x=15, y=485, width=10, height=50)


paso8_btn = tk.Button(opciones_frame, text="Paso 8", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
paso8_btn.place(x=30, y=540)
paso8_indicador = tk.Label(opciones_frame, text="", bg='#9b9b9b', font=('Arial', 12, 'bold'))
paso8_indicador.place(x=15, y=540, width=10, height=50)


opciones_frame.pack(side=tk.LEFT)
opciones_frame.pack_propagate(False)
opciones_frame.config(width=300, height=700)

main_frame = tk.Frame(root, bg='#e6e6e6', highlightbackground="black", highlightthickness=1)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.config(width=800, height=700)

root.mainloop()
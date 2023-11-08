import tkinter as tk

root = tk.Tk()

root.geometry("1100x700")
root.title("Pizzería DELIZIOSO")

opciones_frame = tk.Frame(root, bg='#c2c2c2')

inicio_btn = tk.Button(opciones_frame, text="Inicio", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
inicio_btn.place(x=30, y=100)

paso1_btn = tk.Button(opciones_frame, text="Paso 1", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
paso1_btn.place(x=30, y=155)

paso2_btn = tk.Button(opciones_frame, text="Paso 2", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
paso2_btn.place(x=30, y=210)

paso3_btn = tk.Button(opciones_frame, text="Paso 3", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
paso3_btn.place(x=30, y=265)

paso4_btn = tk.Button(opciones_frame, text="Paso 4", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
paso4_btn.place(x=30, y=320)

paso5_btn = tk.Button(opciones_frame, text="Paso 5", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
paso5_btn.place(x=30, y=375)

paso6_btn = tk.Button(opciones_frame, text="Paso 6", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
paso6_btn.place(x=30, y=430)

paso7_btn = tk.Button(opciones_frame, text="Paso 7", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
paso7_btn.place(x=30, y=485)

paso8_btn = tk.Button(opciones_frame, text="Paso 8", width=20, height=2, bg='#c2c2c2', font=('Arial', 12, 'bold'))
paso8_btn.place(x=30, y=540)

opciones_frame.pack(side=tk.LEFT)
opciones_frame.pack_propagate(False)
opciones_frame.config(width=300, height=700)

main_frame = tk.Frame(root, bg='#e6e6e6', highlightbackground="black", highlightthickness=1)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.config(width=800, height=700)

root.mainloop()
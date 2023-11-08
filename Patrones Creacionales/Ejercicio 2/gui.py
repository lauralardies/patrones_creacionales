import tkinter as tk

# ------------------------------- VARIABLES GLOBALES ----------------------------------

color_fondo = '#F2F2F2'
color_header = '#FFA500'

# ------------------------------- VENTANA PRINCIPAL ----------------------------------

class TkinterApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1100x700")
        self.resizable(0, 0)
        self.title("Pizzeria DELIZIOSO")
        self.config(background= color_fondo)
    
    # ---------------- HEADER ------------------------

        self.header = tk.Frame(self, bg=color_header)
        self.header.place(relx=0, rely=0, relwidth=1.0, relheight=0.1)
        
    # --------------------  MAIN FRAME ---------------------------

        main_frame = tk.Frame(self)
        main_frame.place(relx=0, rely=0.1, relwidth=1.0, relheight=0.9)



root = TkinterApp()
root.mainloop()
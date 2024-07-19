import tkinter as tk
from tkinter import messagebox
import random

class Ahorcado:
    def __init__(self, root, palabra_secreta):
        self.root = root
        self.root.title("Juego del Ahorcado")
        self.palabra_secreta = palabra_secreta
        self.palabra_mostrada = ["_" for _ in self.palabra_secreta]
        self.intentos = 6

        # Configuración de los elementos gráficos
        self.label_palabra = tk.Label(root, text=" ".join(self.palabra_mostrada), font=("Helvetica", 24))
        self.label_palabra.pack(pady=20)
        
        self.label_intentos = tk.Label(root, text=f"Intentos restantes: {self.intentos}", font=("Helvetica", 14))
        self.label_intentos.pack(pady=10)
        
        self.entrada_letra = tk.Entry(root, font=("Helvetica", 18))
        self.entrada_letra.pack(pady=20)
        self.entrada_letra.bind('<Return>', self.adivinar)

        self.boton_adivinar = tk.Button(root, text="Adivinar", command=self.adivinar, font=("Helvetica", 18))
        self.boton_adivinar.pack(pady=10)

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack(pady=20)
        self.dibujar_base()

    def dibujar_base(self):
        # Dibujar la base de la horca
        self.canvas.create_line(50, 350, 150, 350, width=5)  # Base
        self.canvas.create_line(100, 350, 100, 50, width=5)  # Poste vertical
        self.canvas.create_line(100, 50, 250, 50, width=5)   # Poste horizontal
        self.canvas.create_line(250, 50, 250, 100, width=5)  # Cuerda

    def dibujar_ahorcado(self):
        errores = 6 - self.intentos
        if errores >= 1:
            self.canvas.create_oval(225, 100, 275, 150, width=5)  # Cabeza
        if errores >= 2:
            self.canvas.create_line(250, 150, 250, 250, width=5)  # Cuerpo
        if errores >= 3:
            self.canvas.create_line(250, 180, 200, 220, width=5)  # Brazo izquierdo
        if errores >= 4:
            self.canvas.create_line(250, 180, 300, 220, width=5)  # Brazo derecho
        if errores >= 5:
            self.canvas.create_line(250, 250, 200, 300, width=5)  # Pierna izquierda
        if errores >= 6:
            self.canvas.create_line(250, 250, 300, 300, width=5)  # Pierna derecha

    def adivinar(self, event=None):
        letra = self.entrada_letra.get().lower()
        self.entrada_letra.delete(0, tk.END)

        if len(letra) == 1 and letra.isalpha():
            if letra in self.palabra_secreta:
                for idx, char in enumerate(self.palabra_secreta):
                    if char == letra:
                        self.palabra_mostrada[idx] = letra
            else:
                self.intentos -= 1

            self.actualizar_estado()
        else:
            messagebox.showwarning("Entrada inválida", "Por favor ingresa una sola letra.")

    def actualizar_estado(self):
        self.label_palabra.config(text=" ".join(self.palabra_mostrada))
        self.label_intentos.config(text=f"Intentos restantes: {self.intentos}")
        self.dibujar_ahorcado()

        if "_" not in self.palabra_mostrada:
            messagebox.showinfo("¡Ganaste!", f"Felicidades, ganaste! La palabra era: {self.palabra_secreta}")
            self.root.quit()
        elif self.intentos <= 0:
            messagebox.showinfo("¡Perdiste!", f"Lo siento, has perdido. La palabra era: {self.palabra_secreta}")
            self.root.quit()

# Ventana para ingresar la palabra secreta
def ingresar_palabra_secreta():
    def iniciar_juego():
        palabra_secreta = entrada_palabra.get().lower()
        ventana_ingreso.destroy()
        root = tk.Tk()
        juego = Ahorcado(root, palabra_secreta)
        root.mainloop()

    ventana_ingreso = tk.Tk()
    ventana_ingreso.title("Ingresar palabra secreta")

    label_ingreso = tk.Label(ventana_ingreso, text="Ingresa la palabra secreta:", font=("Helvetica", 14))
    label_ingreso.pack(pady=10)
    
    entrada_palabra = tk.Entry(ventana_ingreso, font=("Helvetica", 18))
    entrada_palabra.pack(pady=10)
    
    boton_ingresar = tk.Button(ventana_ingreso, text="Iniciar Juego", command=iniciar_juego, font=("Helvetica", 14))
    boton_ingresar.pack(pady=10)
    
    ventana_ingreso.mainloop()

# Comenzar la aplicación
ingresar_palabra_secreta()


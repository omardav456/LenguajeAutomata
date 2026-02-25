import customtkinter as ctk
import tkinter as tk
from drawing.shapes import Shapes


class App:

    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.geometry("900x600")
        self.root.title("Autómata Dibujante")

        # Variables del autómata
        self.palabra = ""
        self.indice = 0

        self.setup_ui()

    # ==============================
    # UI
    # ==============================

    def setup_ui(self):

        # Frame inferior
        self.frameEntry = ctk.CTkFrame(self.root, height=100)
        self.frameEntry.pack(side="bottom", fill="x", padx=10, pady=10)

        self.entry = ctk.CTkEntry(
            self.frameEntry,
            placeholder_text="Ingrese palabra del autómata"
        )
        self.entry.pack(side="left", padx=10, pady=10)

        self.entry.bind("<Return>", self.iniciar)

        self.btn = ctk.CTkButton(
            self.frameEntry,
            text="Ejecutar",
            command=self.iniciar
        )
        self.btn.pack(side="left", padx=10)

        # Canvas principal
        self.canvas = tk.Canvas(
            self.root,
            width=800,
            height=450,
            bg="white"
        )
        self.canvas.pack(pady=10)

        # Motor de dibujo
        self.drawer = Shapes(self.canvas)

    # ==============================
    # Control del Autómata
    # ==============================

    def iniciar(self, event=None):
        """Inicia el procesamiento del autómata"""
        self.canvas.delete("all")
        self.palabra = self.entry.get().upper()
        self.indice = 0
        self.procesar_simbolo()

    def procesar_simbolo(self):
        """Procesa símbolo por símbolo respetando el orden"""

        if self.indice >= len(self.palabra):
            return  # Termina cuando ya no hay más símbolos

        simbolo = self.palabra[self.indice]

        # Transiciones del autómata
        if simbolo in ['S', 'M', 'L']:
            self.drawer.set_size(simbolo)

        elif simbolo == 'C':
            self.drawer.draw_square()

        elif simbolo == 'T':
            self.drawer.draw_triangle()

        elif simbolo == 'R':
            self.drawer.draw_rectangle()

        elif simbolo == 'G':
            self.drawer.rotate()

        # Avanza al siguiente símbolo
        self.indice += 1

        # Espera 600 ms antes de procesar el siguiente
        self.root.after(600, self.procesar_simbolo)

    # ==============================
    # Ejecutar app
    # ==============================

    def run(self):
        self.root.mainloop()
import random
import customtkinter as ctk
import tkinter as tk
from drawing.shapes import Shapes
from automata.automata import Automata
from core.automata_controller import AutomataController


class App:

    def __init__(self, automata):
        self.automata = automata

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.geometry("900x600")
        self.root.title("Autómata Dibujante")

        # Variables autómata
        self.palabra = ""

        # Variables fondo
        self.fondoTextoId = None
        self.fondoFormas = []
        self.animandoFondo = True

        self.setup_ui()
        self.iniciar_fondo_animado()

    # ==============================
    # UI
    # ==============================

    def setup_ui(self):

        # Canvas de fondo (animación)
        self.canvasFondo = tk.Canvas(
            self.root,
            bg="black",
            highlightthickness=0
        )
        self.canvasFondo.place(relwidth=1, relheight=1)

        # Canvas del autómata (encima)
        self.canvas = tk.Canvas(
            self.root,
            width=800,
            height=450,
            bg="white",
            highlightthickness=0
        )
        self.canvas.place(relx=0.5, rely=0.4, anchor="center")

        # Frame inferior
        self.frameEntry = ctk.CTkFrame(self.root, height=100)
        self.frameEntry.pack(side="bottom", fill="x", padx=10, pady=10)

        self.entry = ctk.CTkEntry(
            self.frameEntry,
            placeholder_text="Ingrese palabra del autómata"
        )
        self.entry.pack(pady=10)

        self.entry.bind("<Return>", self.iniciar)


        # Motor de dibujo
        self.drawer = Shapes(self.canvas)

    # ==============================
    # Control Autómata
    # ==============================

    def iniciar(self, event=None):
        # Solo borrar lo del autómata
        self.canvas.delete("automata")
        self.palabra = self.entry.get().strip().upper()
        shapes = Shapes(self.canvas)
        automataC = AutomataController(
            automata=self.automata,
            shapes=shapes
        )
        automataC.iniciar(palabra=self.palabra)

    # ==============================
    # Fondo Animado
    # ==============================

    def iniciar_fondo_animado(self):

        width = self.root.winfo_width()
        height = self.root.winfo_height()

        self.fondoTextoId = self.canvasFondo.create_text(
            -500,
            height - 100,
            text="Hecho por Omar Quintero y Néstor Fula",
            fill="#cccccc",
            font=("Helvetica", 16, "bold")
        )

        self.canvasFondo.tag_lower(self.fondoTextoId)

        self.animar_fondo()

    def animar_fondo(self):

        if not self.animandoFondo:
            return

        width = self.root.winfo_width()

        coords = self.canvasFondo.coords(self.fondoTextoId)
        if coords:
            self.canvasFondo.move(self.fondoTextoId, 2, 0)
            x = coords[0]

            if x > width + 400:
                height = self.root.winfo_height()
                self.canvasFondo.coords(
                    self.fondoTextoId,
                    -400,
                    height - 30
                )

        if random.random() < 0.05:
            self.crear_forma_fondo()

        for forma in self.fondoFormas:
            self.canvasFondo.move(forma, 0, 0.5)

        self.root.after(40, self.animar_fondo)

    def crear_forma_fondo(self):

        width = self.root.winfo_width()

        x = random.randint(0, width)
        y = -10

        tamaño = random.randint(2, 5)

        forma = self.canvasFondo.create_oval(
            x, y, x+tamaño, y+tamaño,
            fill="#00ffff",
            outline=""
        )

        self.fondoFormas.append(forma)
    # ==============================
    # Ejecutar
    # ==============================

    def run(self):
        self.root.mainloop()
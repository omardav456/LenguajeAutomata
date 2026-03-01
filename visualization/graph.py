import tkinter as tk
from automata.automata import Automata
from automata.transitions import TransitionFunction, TransitionTable
import math

class GrafoAutomata:
    
    def __init__(self, canvas):
        self.canvas= canvas
        self.posiciones={}
        
    def dibujar(self, automata):

        self.canvas.delete("all")
        self.posiciones = {}
        print("dIBUJANDO")
        estados = automata.getEstados()
        transiciones = automata.getFuncionTransicion().getTransiciones()

        n = len(estados)
        centro_x = 200
        centro_y = 170
        radio = 120

        # =========================
        # POSICIONAR EN CÍRCULO
        # =========================
        for i, estado in enumerate(estados):
            angulo = 2 * math.pi * i / n
            x = centro_x + radio * math.cos(angulo)
            y = centro_y + radio * math.sin(angulo)
            self.posiciones[estado] = (x, y)

        # =========================
        # AGRUPAR TRANSICIONES
        # =========================
        agrupadas = {}
        transiciones_set = set()

        for t in transiciones:
            clave = (t.estadoActual, t.estadoSiguiente)

            if clave not in agrupadas:
                agrupadas[clave] = []

            agrupadas[clave].append(t.entrada)
            transiciones_set.add(clave)

        # =========================
        # DIBUJAR TRANSICIONES
        # =========================
        for (estadoActual, estadoSiguiente), entradas in agrupadas.items():

            x1, y1 = self.posiciones[estadoActual]
            x2, y2 = self.posiciones[estadoSiguiente]

            # Evitar división por cero (auto-transición simple)
            if estadoActual == estadoSiguiente:
                self.canvas.create_arc(
                    x1-40, y1-40,
                    x1+40, y1+40,
                    start=0,
                    extent=300,
                    style="arc",
                    outline="white",
                    width=2
                )

                self.canvas.create_text(
                    x1,
                    y1-50,
                    text=", ".join(entradas),
                    fill="#00ffff",
                    font=("Arial", 11, "bold")
                )
                continue

            dx = x2 - x1
            dy = y2 - y1
            dist = math.sqrt(dx**2 + dy**2)

            if dist == 0:
                continue

            dx /= dist
            dy /= dist

            radio_estado = 30

            inicio_x = x1 + dx * radio_estado
            inicio_y = y1 + dy * radio_estado

            fin_x = x2 - dx * radio_estado
            fin_y = y2 - dy * radio_estado

            texto = ", ".join(entradas)

            # Si hay transición en ambos sentidos → curva
            if (estadoSiguiente, estadoActual) in transiciones_set:

                offset = 40

                cx = (inicio_x + fin_x) / 2 - dy * offset
                cy = (inicio_y + fin_y) / 2 + dx * offset

                self.canvas.create_line(
                    inicio_x, inicio_y,
                    cx, cy,
                    fin_x, fin_y,
                    smooth=True,
                    arrow="last",
                    width=2,
                    fill="white"
                )

                self.canvas.create_text(
                    cx,
                    cy - 10,
                    text=texto,
                    fill="#00ffff",
                    font=("Arial", 11, "bold")
                )

            else:
                self.canvas.create_line(
                    inicio_x, inicio_y,
                    fin_x, fin_y,
                    arrow="last",
                    width=2,
                    fill="white"
                )

                tx = (inicio_x + fin_x) / 2
                ty = (inicio_y + fin_y) / 2 - 10

                self.canvas.create_text(
                    tx,
                    ty,
                    text=texto,
                    fill="#00ffff",
                    font=("Arial", 11, "bold")
                )

        # =========================
        # DIBUJAR ESTADOS
        # =========================
        for estado in estados:

            x, y = self.posiciones[estado]

            self.canvas.create_oval(
                x-30, y-30,
                x+30, y+30,
                fill="#1e1e1e",
                outline="#00bfff",
                width=3
            )

            if estado in automata.aceptacion:
                self.canvas.create_oval(
                    x-24, y-24,
                    x+24, y+24,
                    outline="yellow",
                    width=3
                )

            self.canvas.create_text(
                x, y,
                text=estado,
                fill="white",
                font=("Arial", 14, "bold")
            )

        # =========================
        # FLECHA ESTADO INICIAL
        # =========================
        x0, y0 = self.posiciones[automata.qCero]

        self.canvas.create_line(
            x0-80, y0,
            x0-30, y0,
            arrow="last",
            width=3,
            fill="green"
        )
        print("OU YEAJ")
        # =========================
        # TABLA
        # =========================
        self.mostrar_tabla(automata)
            
    def mostrar_tabla(self, automata):

        y_inicio = 380
        x_inicio = 200
        salto = 20

        self.canvas.create_text(
            x_inicio, y_inicio-25,
            text="Función de Transición",
            fill="white",
            font=("Arial", 14, "bold")
        )

        for i, t in enumerate(automata.funcionTransicion.transicions):

            texto = f"δ({t.estadoActual}, {t.entrada}) → {t.estadoSiguiente}"

            self.canvas.create_text(
                x_inicio,
                y_inicio + i * salto,
                text=texto,
                fill="#cccccc",
                font=("Consolas", 11)
            )
    
    def mostrar_no_pertenece(self):

        self.canvas.delete("all")

        # Texto principal
        self.canvas.create_text(
            200,
            60,
            text="NO PERTENECE",
            fill="red",
            font=("Arial", 26, "bold")
        )

        # Cara (círculo)
        self.canvas.create_oval(
            150, 100,
            250, 200,
            fill="white",
            outline="black",
            width=2
        )

        # Ojos
        self.canvas.create_oval(170, 130, 185, 145, fill="black")
        self.canvas.create_oval(215, 130, 230, 145, fill="black")

        # Boca triste
        self.canvas.create_arc(
            170, 150,
            230, 190,
            start=0,
            extent=180,
            style="arc",
            width=3
        )

        # Texto tipo meme abajo
        self.canvas.create_text(
            200,
            230,
            text="AUTÓMATA ENOJADO 😡",
            fill="white",
            font=("Arial", 14, "bold")
        )

            
            
'''           
            
alfabeto= {
    "S",
    "M",
    "L",
    "C",
    "T",
    "R",
    "A",
    "G"}
t1 = TransitionFunction("q0", "S", "q1")
t2 = TransitionFunction("q0", "M", "q1")
t3 = TransitionFunction("q0", "L", "q1")
t4 = TransitionFunction("q1", "C", "q2")
t5 = TransitionFunction("q1", "T", "q2")
t6 = TransitionFunction("q1", "R", "q2")
t7 = TransitionFunction("q2", "A", "q3")
t8 = TransitionFunction("q3", "G", "q2")

tabla = TransitionTable([t1, t2, t3, t4, t5, t6, t7, t8])

automata = Automata(
    alfabeto=alfabeto,
    estados={"q0","q1","q2","q3"},
    qCero="q0",
    aceptacion={"q3", "q2"},
    funcionTransicion=tabla
)

canvas= tk.Canvas(
            width=800,
            height=450,
            bg="white",
            highlightthickness=0
        )
grafo= GrafoAutomata(canvas)
grafo.dibujar(automata)
#Hace validacion 
'''
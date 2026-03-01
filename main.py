import customtkinter as ctk
from automata.automata import Automata
from automata.transitions import TransitionFunction, TransitionTable
from core.automata_controller import AutomataController
from drawing.shapes import Shapes
from ui.app import App

alfabeto= {
    "S",
    "M",
    "L",
    "C",
    "T",
    "E",
    "A",
    "G"}
t1 = TransitionFunction("q0", "S", "q1")
t2 = TransitionFunction("q0", "M", "q1")
t3 = TransitionFunction("q0", "L", "q1")
t4 = TransitionFunction("q1", "C", "q2")
t5 = TransitionFunction("q1", "T", "q2")
t6 = TransitionFunction("q1", "E", "q2")
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

print(automata.procesar("LEAGAGAGA"))
#Hace validacion 
app = App(automata)
app.run()



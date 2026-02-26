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

print(automata.procesar("LTAGAGAGA"))
#Hace validacion 
app = App(automata)
app.run()
shapes= Shapes(app.getCanvas)
print("Holi")
automataC= AutomataController(automata=automata, shapes=shapes)
automataC.siguientePaso("q0", "1")
'''
def guardar(event):
    # Obtener texto
    texto = entrada.get()
    print(f"Texto guardado: {texto}")
    # Opcional: limpiar entrada
    entrada.delete(0, 'end')
    



#REGLAS
alfabeto=[
    'A', #Avanzar
    'G', #Giro
    'S', #Pequeño
    'M', #Mediano
    'L', #Grande
    'T', #Triangulo
    'C', #Cuadrado
    'R' #Rectangulo
]
estados=[
    'Q0', #Inicial
    'Q1', #Tamaño
    'Q2', #Figura
    'Q3', #Dibujar
    'Q4', #Girar
    'Q5', #Aceptar
]
qCero=estados[0]
F= [
    'Q5'
]

#Funcion de transicion y reglas
# Creamos transiciones
t1 = TransitionFunction('Q0', 'S', 'Q1')
t2 = TransitionFunction('Q0', 'M', 'Q1')
t3 = TransitionFunction('Q0', 'L', 'Q1')
t4 = TransitionFunction('Q1', 'T', 'Q2')
t5 = TransitionFunction('Q1', 'C', 'Q2')
t6 = TransitionFunction('Q1', 'R', 'Q2')
t7 = TransitionFunction('Q2', 'A', 'Q3')
t8 = TransitionFunction('Q3', 'G', 'Q4')
t9 = TransitionFunction('Q3', 'A', 'Q5')
t10 = TransitionFunction('Q4', 'A', 'Q3')

# Creamos la tabla
tabla = TransitionTable([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10])

# Probamos
estado_actual = 'q1'
entrada = 'A'

siguiente = tabla.getNextState(estado_actual, entrada)

print("Siguiente estado:", siguiente)


app = App()
app.run()



# Ventana
app = ctk.CTk()
app.geometry("300x150")

# Campo de entrada
entrada = ctk.CTkEntry(app, placeholder_text="Escribe y pulsa Enter...")
entrada.pack(pady=20)

# Enter
entrada.bind('<Return>', guardar)

app.mainloop()

'''
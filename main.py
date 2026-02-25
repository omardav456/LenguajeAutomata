import customtkinter as ctk
from automata.automata import Automata
from automata.transitions import TransitionFunction, TransitionTable
from ui.app import App
'''
def guardar(event):
    # Obtener texto
    texto = entrada.get()
    print(f"Texto guardado: {texto}")
    # Opcional: limpiar entrada
    entrada.delete(0, 'end')
'''    



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

'''

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
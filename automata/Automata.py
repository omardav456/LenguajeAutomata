

class Automata:
    def __init__(self,alfabeto=None, estados=None, qCero='', F=None, funcionTransicion=None):
        pass
    

#REGLAS
alfabeto=[
    'C', #Cuadrado
    'T', #Triangulo
    'R', #Rectangulo
]
estados=[
    'Q0',
    'Q1', #Dibujar linea
    'Q2', #Girar x cantidad
    'Q3', #Estado de aceptación
]
qCero=estados[0]
F= [
    'Q3'
]



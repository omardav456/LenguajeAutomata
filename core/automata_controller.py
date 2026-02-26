
from automata.automata import Automata
from automata.transitions import TransitionTable
from drawing.shapes import Shapes
class AutomataController:
    
    def __init__(self, automata, shapes=None):
        self.automata= automata
        self.funcionTransicion = self.automata.getFuncionTransicion()
        self.shapes= shapes
    
    def siguientePaso(self, state, word):
        if self.funcionTransicion.getNextState(state,word)==None:
            self.shapes.errores("ERROR PAPU")
            print("Error")
    
    def iniciar(self, palabra):
        linea= palabra[0]
        figure= palabra[1]
        for simbolo in palabra:
            if simbolo=='A':
                self.shapes.avanzar()
                self.shapes.error("Avanzar")
            elif simbolo=='G':
                self.shapes.girar(90)
                self.shapes.avanzar()
                self.shapes.error("Girar 90°")
        
        
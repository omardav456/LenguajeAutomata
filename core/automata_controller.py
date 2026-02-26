
from automata.automata import Automata
from automata.transitions import TransitionTable
from drawing.shapes import Shapes
class AutomataController:
    
    def __init__(self, automata, shapes=None):
        self.automata= automata
        self.funcionTransicion = self.automata.getFuncionTransicion()
        self.shapes= shapes
    
    def pertenece(self, word):
        if self.automata.procesar(word):
            self.shapes.cumpleAutomata("Pertenece", "green")
            return True
        else:
            self.shapes.cumpleAutomata("NO Pertenece", "red")
            return False
    
    def iniciar(self, palabra):
        self.shapes.canvas.delete("all")
        size= palabra[0]
        print(size)
        self.shapes.setSize(size)
        print("ta bien")
        figure= palabra[1]
        if figure=="T":
            angulo=120
        else:
            angulo=90
        self.shapes.escribir(palabra, primary=True)
        if self.pertenece(palabra)== False:
            return 
        for simbolo in palabra:
            if simbolo=='A':
                self.shapes.avanzar()
                self.shapes.escribir("Avanzar")
            elif simbolo=='G':
                self.shapes.girar(angulo)
                self.shapes.escribir(f"Girar {angulo}°")
        
        
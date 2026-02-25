from .transitions import TransitionFunction, TransitionTable

class Automata:
    def __init__(self,alfabeto=None, estados=None, qCero='', aceptacion=None, funcionTransicion=None):
        self.alfabeto=alfabeto
        self.estados=estados
        self.qCero= qCero
        self.aceptacion=aceptacion
        self.funcionTransicion= funcionTransicion
        
    

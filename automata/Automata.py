

class Automata:
    def __init__(self,alfabeto=None, estados=None, qCero='', aceptacion=None, funcionTransicion=None):
        self.alfabeto=alfabeto
        self.estados=estados
        self.qCero= qCero
        self.aceptacion=aceptacion
        self.funcionTransicion= funcionTransicion
    
    def getFuncionTransicion(self):
        return self.funcionTransicion
    def procesar(self, word):
        estadoActual= self.qCero
        for simbolo in word:
            
            if simbolo not in self.alfabeto:
                return False
            siguienteEstado= self.funcionTransicion.getNextState(estadoActual,simbolo)
            if siguienteEstado is None:
                return False
            estadoActual=siguienteEstado
        return estadoActual in self.aceptacion  

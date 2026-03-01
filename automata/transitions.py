

class TransitionFunction:
    def __init__(self,estadoActual='', entrada='', estadoSiguiente='' ):
        self.estadoActual=estadoActual
        self.entrada=entrada
        self.estadoSiguiente= estadoSiguiente
    
    
    

class TransitionTable:
    def __init__(self, listadeTransitionFunction= None):
        if listadeTransitionFunction==None:
            self.transicions=[]
        else: 
            self.transicions=listadeTransitionFunction
    
    def getTransiciones(self):
        return self.transicions
    
    def getNextState(self, estadoActual, entrada):
        for transicion in self.transicions:
            if transicion.estadoActual == estadoActual and transicion.entrada == entrada :
                return transicion.estadoSiguiente
            
        return None

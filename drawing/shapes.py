import math
class Shapes:

    def __init__(self, canvas):
        self.canvas = canvas
        self.x = int(self.canvas["width"])/2 +30
        self.y = int(self.canvas["height"])/2
        self.angle = 0
        self.step = 50
        self.messageId= None
        self.tituloId= None
        self.messageAutomataId= None
        self.color= "black"

    def setColor(self, color):
        self.color= color
        
    def cumpleAutomata(self, resultado, color):
        if self.messageAutomataId!=None:
                self.canvas.delete("resultado")
        self.messageAutomataId =self.canvas.create_text(
                250, 285,
                text=resultado,
                fill=color,
                font=("Arial", 14),
                tags="resultado"
            )
        
    def avanzar(self):
        rad = math.radians(self.angle)

        new_x = self.x + self.step * math.cos(rad)
        new_y = self.y - self.step * math.sin(rad)

        self.canvas.create_line(
            self.x, 
            self.y, 
            new_x, 
            new_y,
            fill= self.color
        )

        self.x = new_x
        self.y = new_y

    def girar(self, grados):
        self.angle += grados
        
    def escribir(self, mensaje, primary=False):
        if primary:
            if self.tituloId is not None:
                self.canvas.delete("titulo")
            ancho = self.canvas.winfo_width()
            self.tituloId = self.canvas.create_text(
                ancho//2, 20,
                text=mensaje,
                fill="blue",
                font=("Arial", 18, "bold"),
                tags="titulo"
            )
        else:
            if self.messageId!=None:
                self.canvas.delete(self.messageId)
            
            self.messageId = self.canvas.create_text(
                200, 20,
                text=mensaje,
                fill="black",
                font=("Arial", 14)
            )
    
    def setSize(self, symbol):
        if symbol == "S":
            self.step = 30
        elif symbol == "M":
            self.step = 100
        elif symbol == "L":
            self.step = 180
        
        

   
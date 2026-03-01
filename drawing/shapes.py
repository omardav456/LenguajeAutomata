import math
import tkinter as tk
import random
class Shapes:

    def __init__(self, canvas):
        self.canvas = canvas
        self.x = int(self.canvas["width"])/2 -100
        self.y = int(self.canvas["height"])/2 +100
        self.angle = 0
        self.step = 50
        self.messageId= None
        self.tituloId= None
        
        self.messageAutomataId= None
        self.color= "black"

    def setColorRandom(self):
        color = "#%06x" % random.randint(0, 0xFFFFFF)
        self.color= color
        
    def cumpleAutomata(self, resultado, color):
        if self.messageAutomataId!=None:
                self.canvas.delete("resultado")
        ancho = ancho = self.canvas.winfo_width()
        self.messageAutomataId =self.canvas.create_text(
                ancho//2, 100,
                text=resultado,
                fill=color,
                font=("Arial", 16),
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
            fill= self.color,
            width=3,
            arrow= tk.LAST
        )

        self.x = new_x
        self.y = new_y

    def girar(self, grados):
        self.angle += grados
        
    def escribir(self, mensaje, primary=False):
        ancho = self.canvas.winfo_width()
        if primary:
            if self.tituloId is not None:
                self.canvas.delete("titulo")
            
            self.tituloId = self.canvas.create_text(
                ancho//2, 20,
                text=mensaje,
                fill="blue",
                font=("Arial", 20, "bold"),
                tags="titulo"
            )
        else:
            if self.messageId!=None:
                self.canvas.delete(self.messageId)
            
            self.messageId = self.canvas.create_text(
                ancho//2, 60,
                text=mensaje,
                fill="black",
                font=("Arial", 15)
            )
    
    def setSize(self, symbol):
        if symbol == "S":
            self.step = 130
        elif symbol == "M":
            self.step = 180
        elif symbol == "L":
            self.step = 220
        
        

   
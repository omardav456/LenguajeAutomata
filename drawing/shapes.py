import math
class Shapes:

    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 200
        self.y = 200
        self.angle = 0
        self.step = 50

    def avanzar(self):
        rad = math.radians(self.angle)

        new_x = self.x + self.step * math.cos(rad)
        new_y = self.y - self.step * math.sin(rad)

        self.canvas.create_line(self.x, self.y, new_x, new_y)

        self.x = new_x
        self.y = new_y

    def girar(self, grados):
        self.angle += grados
        
    def errores(self, mensaje):
        self.canvas.create_text(
            200, 20,
            text=mensaje,
            fill="black",
            font=("Arial", 14)
        )
    
    def set_size(self, size_symbol):
        if size_symbol == 'S':
            self.size = 30
        elif size_symbol == 'M':
            self.size = 60
        elif size_symbol == 'L':
            self.size = 100

   
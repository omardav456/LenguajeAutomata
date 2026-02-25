class Shapes:

    def __init__(self, canvas):
        self.canvas = canvas
        self.size = 50
        self.x = 100
        self.y = 100
        self.angle = 0

    def set_size(self, size_symbol):
        if size_symbol == 'S':
            self.size = 30
        elif size_symbol == 'M':
            self.size = 60
        elif size_symbol == 'L':
            self.size = 100

    def draw_square(self):
        self.canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.size,
            self.y + self.size,
            fill="blue"
        )

    def draw_triangle(self):
        self.canvas.create_polygon(
            self.x, self.y,
            self.x + self.size, self.y,
            self.x + self.size/2, self.y - self.size,
            fill="green"
        )

    def draw_rectangle(self):
        self.canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.size * 1.5,
            self.y + self.size,
            fill="red"
        )

    def rotate(self):
        self.x += 20
        self.y += 20
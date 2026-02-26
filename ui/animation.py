import customtkinter as ctk
import tkinter as tk
import random

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Animación Omar")
app.geometry("900x400")

width = 900
height = 400

# Canvas normal dentro de CustomTkinter
canvas = tk.Canvas(app, width=width, height=height, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

texto = "Hecho por Omar Quintero y Néstor Fula"

text_id = canvas.create_text(
    -400, height // 2,
    text=texto,
    fill="white",
    font=("Helvetica", 26, "bold")
)

velocidad = 4
formas = []

def crear_forma():
    x = random.randint(0, width)
    y = random.randint(0, height)
    tamaño = random.randint(20, 50)
    color = random.choice(["red", "cyan", "yellow", "green", "orange", "purple"])

    tipo = random.choice(["circulo", "cuadrado", "triangulo", "tortuga"])

    if tipo == "circulo":
        forma = canvas.create_oval(x, y, x+tamaño, y+tamaño, outline=color)

    elif tipo == "cuadrado":
        forma = canvas.create_rectangle(x, y, x+tamaño, y+tamaño, outline=color)

    elif tipo == "triangulo":
        forma = canvas.create_polygon(
            x, y,
            x+tamaño, y,
            x+tamaño//2, y-tamaño,
            outline=color,
            fill=""
        )

    elif tipo == "tortuga":
        cuerpo = canvas.create_oval(x, y, x+tamaño, y+tamaño, outline=color)
        cabeza = canvas.create_oval(
            x+tamaño, y+tamaño//3,
            x+tamaño + tamaño//3, y+tamaño//1.5,
            outline=color
        )
        formas.append(cabeza)
        forma = cuerpo

    formas.append(forma)

def animar():
    canvas.move(text_id, velocidad, 0)
    x = canvas.coords(text_id)[0]

    if x > width + 400:
        canvas.coords(text_id, -400, height // 2)

    if random.random() < 0.08:
        crear_forma()

    for forma in formas:
        canvas.move(forma, 0, 1)

    app.after(30, animar)

animar()
app.mainloop()
import customtkinter as ctk

def guardar(event):
    # Obtener texto
    texto = entrada.get()
    print(f"Texto guardado: {texto}")
    # Opcional: limpiar entrada
    entrada.delete(0, 'end')

# Ventana
app = ctk.CTk()
app.geometry("300x150")

# Campo de entrada
entrada = ctk.CTkEntry(app, placeholder_text="Escribe y pulsa Enter...")
entrada.pack(pady=20)

# Enter
entrada.bind('<Return>', guardar)

app.mainloop()

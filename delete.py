import customtkinter as ctk

# Crear una ventana con customtkinter
root = ctk.CustomTk()

# Obtener la altura de la ventana
height = root.winfo_height()

# Imprimir la altura
print("Altura de la ventana:", height)

# Ejecutar el bucle de eventos de customtkinter
root.mainloop()

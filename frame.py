import tkinter as tk

def obtener_valor():
    # Obtener el valor de la entrada
    valor = entrada.get()
    # Hacer algo con el valor (en este caso, imprimirlo)
    print("El valor del Entry es:", valor)

# Crear una ventana Tkinter
ventana = tk.Tk()

# Crear una variable StringVar para almacenar el valor del Entry
valor_entry = tk.StringVar()

# Crear un Entry y asociarlo con la variable StringVar
entrada = tk.Entry(ventana, textvariable=valor_entry)
entrada.pack()

# Crear un botón para llamar a la función obtener_valor
boton = tk.Button(ventana, text="Obtener valor", command=obtener_valor)
boton.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()

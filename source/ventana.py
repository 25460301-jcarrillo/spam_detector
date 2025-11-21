import tkinter as tk   
from tkinter import messagebox


ventana = tk.Tk()
ventana.title("ventana simple")

label = tk.Label(ventana, text="Hola mundo") # widget de texto
label.pack(pady=10) # la coloca en la ventana 

label = tk.Label(ventana, text="Presiona el boton") # widget de texto
label.pack(pady=10) # la coloca en la ventana 

def mostrar_mensaje():
    messagebox.showinfo("Aviso", "Boton presionado")

boton = tk.Button(ventana, text="Haz click aqui", command=mostrar_mensaje, font=("Arial",50))
boton.pack(pady=10)



ventana.mainloop() # ciclo que permite a la venta estar activa
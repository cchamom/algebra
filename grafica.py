import tkinter as tk
from tkinter import Label, Entry, Button
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graficar_sistema():
    a1 = float(entry_a1.get())
    b1 = float(entry_b1.get())
    c1 = float(entry_c1.get())
    a2 = float(entry_a2.get())
    b2 = float(entry_b2.get())
    c2 = float(entry_c2.get())

    def ecuacion1(x):
        return (-a1 * x + c1) / b1

    def ecuacion2(x):
        return (-a2 * x + c2) / b2

    x = np.linspace(-10, 10, 100)
    y1 = ecuacion1(x)
    y2 = ecuacion2(x)

    plt.figure(figsize=(6, 6))
    plt.plot(x, y1, label='Ecuación numero 1')
    plt.plot(x, y2, label='Ecuación numero 2')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('SISTEMA DE ECUACIONES')

    canvas = FigureCanvasTkAgg(plt.gcf(), master=ventana)
    canvas.draw()
    canvas.get_tk_widget().grid(row=3, column=0, columnspan=6)

ventana = tk.Tk()
ventana.title("Graficas de Ecuacuaciones")

Label(ventana, text="X: ").grid(row=0, column=0)
Label(ventana, text="Y: ").grid(row=0, column=2)
Label(ventana, text="TI: ").grid(row=0, column=4)
entry_a1 = Entry(ventana)
entry_a1.grid(row=0, column=1)
entry_b1 = Entry(ventana)
entry_b1.grid(row=0, column=3)
entry_c1 = Entry(ventana)
entry_c1.grid(row=0, column=5)

Label(ventana, text="X: ").grid(row=1, column=0)
Label(ventana, text="Y: ").grid(row=1, column=2)
Label(ventana, text="TI: ").grid(row=1, column=4)
entry_a2 = Entry(ventana)
entry_a2.grid(row=1, column=1)
entry_b2 = Entry(ventana)
entry_b2.grid(row=1, column=3)
entry_c2 = Entry(ventana)
entry_c2.grid(row=1, column=5)

Button(ventana, text="GRAFICAR", command=graficar_sistema).grid(row=2, column=0, columnspan=6)

ventana.mainloop()

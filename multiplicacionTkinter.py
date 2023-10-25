import tkinter as tk
import numpy as np

#creamos nuestra ventana principal
class MatrizMultiplicationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiplicación de Matrices")

        self.frame1 = tk.Frame(self.root, bg="navy")
        self.frame1.pack()

    #widget para ingresar los datos de las matrices
        titulo_label = tk.Label(self.frame1, text="Calculadora de Multiplicación de Matrices", bg="navy", font=("Helvetica", 25, "bold"))
        titulo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='n')


        self.filas_A = tk.Label(self.frame1,bg="navy", text="Número de filas de la Matriz A:", fg="white",font=("Helvetica", 12, "bold"))
        self.filas_A.grid(row=1, column=0)
        self.filasA_entry = tk.Entry(self.frame1)
        self.filasA_entry.grid(row=1, column=1)

        self.columnasA = tk.Label(self.frame1,bg="navy", text="Número de columnas de la Matriz A:", fg="white", font=("Helvetica", 12, "bold"))
        self.columnasA.grid(row=2, column=0)
        self.columnasA_entry = tk.Entry(self.frame1)
        self.columnasA_entry.grid(row=2, column=1)

        self.filasB = tk.Label(self.frame1,bg="navy", text="Número de filas de la Matriz B:", fg="white", font=("Helvetica", 12, "bold"))
        self.filasB.grid(row=3, column=0)
        self.filasB_entry = tk.Entry(self.frame1)
        self.filasB_entry.grid(row=3, column=1)

        self.columnasB = tk.Label(self.frame1,bg="navy", text="Número de columnas de la Matriz B:", fg="white", font=("Helvetica", 12, "bold"))
        self.columnasB.grid(row=4, column=0)
        self.columnasB_entry = tk.Entry(self.frame1)
        self.columnasB_entry.grid(row=4, column=1)

        self.comprobar_button = tk.Button(self.frame1,bg="blue", text="INGRESAR MATRICES", command=self.comprobar, font=("Helvetica", 12, "bold"))
        self.comprobar_button.grid(row=5, columnspan=2, pady=10)

        self.frame2 = tk.Frame(self.root, bg="navy")
        self.frame2.pack()

#label que muestran las matrices en la interfaz
        self.label_matA = tk.Label(self.frame2,bg="navy", text="Matriz A:", fg="white", font=("Helvetica", 12, "bold"))
        self.label_matA.grid(row=0, column=1, pady=10)
        self.label_matB = tk.Label(self.frame2,bg="navy", text="Matriz B:", fg="white", font=("Helvetica", 12, "bold"))
        self.label_matB.grid(row=0, column=2, pady=10)

        self.resultado_label = tk.Label(self.frame2, text="", bg="navy")
        self.resultado_label.grid(row=1, columnspan=2)

#para poder comprobar si las matrices se pueden multiplicar 
    def comprobar(self):
        filasA = int(self.filasA_entry.get())
        columnasA = int(self.columnasA_entry.get())
        filasB = int(self.filasB_entry.get())
        columnasB = int(self.columnasB_entry.get())

        if columnasA != filasB:
            self.resultado_label.config(text="La operacion no se puede realizar por que las filas y las columnas de las matrices no son iguales")
        else:
            self.crear_entradas_matriz(filasA, columnasA, filasB, columnasB)

    def crear_entradas_matriz(self, filasA, columnasA, filasB, columnasB):
        self.matriz_a_entries = []
        self.matriz_b_entries = []

        for i in range(filasA):
            row_entries = []
            for j in range(columnasA):
                entry = tk.Entry(self.frame2)
                entry.grid(row=i + 1, column=j)
                row_entries.append(entry)
            self.matriz_a_entries.append(row_entries)

        for i in range(filasB):
            row_entries = []
            for j in range(columnasB):
                entry = tk.Entry(self.frame2)
                entry.grid(row=i + 1, column=j + columnasA + 1)
                row_entries.append(entry)
            self.matriz_b_entries.append(row_entries)

        calcular_button = tk.Button(self.frame2, text="Calcular", bg="blue", font=("Helvetica", 12, "bold"), command=self.calcular_matrices)
        calcular_button.grid(row=max(filasA, filasB) + 2, columnspan=2, pady=10)

   
    def obtener_valores_matriz(self, entries):
        return [[float(entry.get()) for entry in row] for row in entries]

    def calcular_matrices(self):
        
        matriz_A = self.obtener_valores_matriz(self.matriz_a_entries)
        matriz_B = self.obtener_valores_matriz(self.matriz_b_entries)

        resultado_multiplicacion = np.dot(matriz_A, matriz_B)

    #convertir el resultado en una cadena para mostrarlo en la etiqueta
        resultado_multiplicacion_str = "\n".join(["\t".join(map(str, row)) for row in resultado_multiplicacion])
    
        self.resultado_label.config(text=resultado_multiplicacion_str, bg="royalblue")
        self.resultado_label.grid(row=5, columnspan=2, pady=10)

        self.matC_label = tk.Label(self.frame2, text="Matriz C", bg="royalblue", font=("Helvetica", 12, "bold"))
        self.matC_label.grid(row=4, columnspan=2, pady=10)

    
#cerramos la ventana
if __name__ == "__main__":
    root = tk.Tk()
    app = MatrizMultiplicationApp(root)
    root.geometry("800x500")
    root.config(bg="royalblue")
    root.mainloop() 






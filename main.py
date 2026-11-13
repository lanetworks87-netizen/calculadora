import tkinter as tk
from tkinter import messagebox

from suma import Suma
from resta import Resta
from multiplicacion import Multiplicacion
from division import Division


class CalculadoraApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora colaborativa")
        self.ventana.geometry("370x300")

        tk.Label(self.ventana, text="Numero 1").pack(pady=4)
        self.numero1 = tk.Entry(self.ventana)
        self.numero1.pack()

        tk.Label(self.ventana, text="Numero 2").pack(pady=4)
        self.numero2 = tk.Entry(self.ventana)
        self.numero2.pack()

        botones = tk.Frame(self.ventana)
        botones.pack(pady=20)

        for simbolo, operacion in [
            ("+", Suma),
            ("-", Resta),
            ("*", Multiplicacion),
            ("/", Division),
        ]:
            tk.Button(
                botones,
                text=simbolo,
                width=6,
                command=lambda op=operacion: self.ejecutar(op)
            ).pack(side="left", padx=4)

    def ejecutar(self, clase_operacion):
        try:
            a = float(self.numero1.get())
            b = float(self.numero2.get())
            operacion = clase_operacion()
            resultado = operacion.calcular(a, b)
            messagebox.showinfo("Resultado", str(resultado))
        except ValueError:
            messagebox.showerror("Error", "Ingrese numeros validos")
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir por cero")

    def iniciar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    app = CalculadoraApp()
    app.iniciar()
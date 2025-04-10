import tkinter as tk
import math

def main():
    # Crear ventana principal
    root = tk.Tk()
    root.title("Calculadora de Área de un Círculo")

    # Función para poblar la ventana con widgets
    def populate_main_window():
        # Etiqueta de entrada de radio
        radius_label = tk.Label(root, text="Radio (r):")
        radius_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        # Campo de entrada
        radius_entry = tk.Entry(root)
        radius_entry.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta para el resultado
        result_label = tk.Label(root, text="Área:")
        result_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        result_var = tk.StringVar()
        result_display = tk.Label(root, textvariable=result_var, width=25, anchor="w", relief="sunken")
        result_display.grid(row=1, column=1, padx=10, pady=10)

        # Barra de estado
        status_var = tk.StringVar()
        status_label = tk.Label(root, textvariable=status_var, anchor="w", fg="red", relief="sunken")
        status_label.grid(row=3, column=0, columnspan=2, sticky="we", padx=10, pady=(0,10))

        # Función de cálculo
        def calculate():
            try:
                radius = float(radius_entry.get())
                if radius < 0:
                    raise ValueError("El radio no puede ser negativo.")
                area = math.pi * radius ** 2
                result_var.set(f"{area:.2f}")
                status_var.set("")  # Limpiar barra de estado si todo está bien
            except ValueError:
                result_var.set("")
                status_var.set("⚠️ Entrada no válida. Ingrese un número positivo.")

        # Función para borrar
        def clear():
            radius_entry.delete(0, tk.END)
            result_var.set("")
            status_var.set("")



        # Botones
        calc_button = tk.Button(root, text="Calcular", command=calculate)
        calc_button.grid(row=2, column=0, padx=10, pady=10)

        clear_button = tk.Button(root, text="Borrar", command=clear)
        clear_button.grid(row=2, column=1, padx=10, pady=10)

    populate_main_window()
    root.mainloop()

if __name__ == "__main__":
    main()

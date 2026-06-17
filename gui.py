import cmath
import os
import sys
import tkinter as tk
from tkinter import messagebox

MODULE_ROOT = os.path.dirname(__file__)
sys.path.insert(0, MODULE_ROOT)

from src.logic.calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    root,
    gcd,
    is_prime,
    prime_factors,
    solve_quadratic,
    to_radians,
    sin,
    cos,
    tan,
    log,
    average,
    median,
    mode,
    standard_deviation,
    area_circle,
    area_rectangle,
    area_triangle,
)


class CalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kalkulator matematyczny")
        self.geometry("940x560")
        self.resizable(False, False)

        self.menu_frame = tk.Frame(self, bd=2, relief=tk.GROOVE, padx=10, pady=10)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.content_frame = tk.Frame(self, bd=2, relief=tk.GROOVE, padx=10, pady=10)
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.header_label = tk.Label(self.content_frame, text="Wybierz kategorię obliczeń", font=(None, 16, "bold"))
        self.header_label.pack(anchor="w", pady=(0, 10))

        self.content_area = tk.Frame(self.content_frame)
        self.content_area.pack(fill=tk.BOTH, expand=True)

        self.output_label = tk.Label(self.content_frame, text="", justify=tk.LEFT, anchor="nw", bg="#f3f3f3", bd=1, relief=tk.SUNKEN, padx=8, pady=8, wraplength=620)
        self.output_label.pack(fill=tk.BOTH, pady=(10, 0), expand=False)

        categories = [
            ("Podstawowe działania", self.show_arithmetic),
            ("Potęgi i pierwiastki", self.show_powers),
            ("Trygonometria", self.show_trigonometry),
            ("Logarytmy", self.show_logarithm),
            ("Statystyka", self.show_statistics),
            ("Teoria liczb", self.show_number_theory),
            ("Geometria", self.show_geometry),
            ("Równanie kwadratowe", self.show_quadratic),
        ]

        for text, command in categories:
            btn = tk.Button(self.menu_frame, text=text, width=22, command=command)
            btn.pack(pady=4)

        self.show_arithmetic()

    def clear_content(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()

    def show_output(self, text: str):
        self.output_label.config(text=text)

    def create_entry(self, label_text: str, row: int, default: str = "") -> tk.Entry:
        label = tk.Label(self.content_area, text=label_text)
        label.grid(row=row, column=0, sticky="w", pady=4, padx=(0, 8))
        entry = tk.Entry(self.content_area, width=24)
        entry.grid(row=row, column=1, pady=4, sticky="w")
        entry.insert(0, default)
        return entry

    def show_arithmetic(self):
        self.header_label.config(text="Podstawowe działania arytmetyczne")
        self.clear_content()
        x_entry = self.create_entry("Pierwsza liczba:", 0)
        y_entry = self.create_entry("Druga liczba:", 1)

        def calculate():
            try:
                x = float(x_entry.get())
                y = float(y_entry.get())
            except ValueError:
                messagebox.showerror("Błąd", "Wprowadź poprawne liczby.")
                return

            results = [
                f"Dodawanie: {add(x, y)}",
                f"Odejmowanie: {subtract(x, y)}",
                f"Mnożenie: {multiply(x, y)}",
            ]

            try:
                results.append(f"Dzielenie: {divide(x, y)}")
            except ValueError as error:
                results.append(str(error))

            self.show_output("\n".join(results))

        tk.Button(self.content_area, text="Oblicz", command=calculate, width=20).grid(row=3, column=0, columnspan=2, pady=14)

    def show_powers(self):
        self.header_label.config(text="Potęgi i pierwiastki")
        self.clear_content()
        base_entry = self.create_entry("Podstawa potęgi:", 0)
        exponent_entry = self.create_entry("Wykładnik:", 1)
        value_entry = self.create_entry("Liczba do pierwiastkowania:", 2)
        degree_entry = self.create_entry("Stopień pierwiastka:", 3, "2")

        def calculate():
            try:
                base = float(base_entry.get())
                exponent = float(exponent_entry.get())
                value = float(value_entry.get())
                degree = float(degree_entry.get())
            except ValueError:
                messagebox.showerror("Błąd", "Wprowadź poprawne liczby.")
                return
            try:
                results = [
                    f"Potęga: {power(base, exponent)}",
                    f"Pierwiastek ({degree}-stopnia): {root(value, degree)}",
                ]
            except ValueError as error:
                results = [str(error)]
            self.show_output("\n".join(results))

        tk.Button(self.content_area, text="Oblicz", command=calculate, width=20).grid(row=4, column=0, columnspan=2, pady=14)

    def show_trigonometry(self):
        self.header_label.config(text="Trygonometria")
        self.clear_content()
        angle_entry = self.create_entry("Kąt w stopniach:", 0)

        def calculate():
            try:
                angle = float(angle_entry.get())
            except ValueError:
                messagebox.showerror("Błąd", "Wprowadź poprawny kąt.")
                return
            results = [
                f"sin: {sin(angle)}",
                f"cos: {cos(angle)}",
                f"tan: {tan(angle)}",
                f"radiany: {to_radians(angle)}",
            ]
            self.show_output("\n".join(results))

        tk.Button(self.content_area, text="Oblicz", command=calculate, width=20).grid(row=1, column=0, columnspan=2, pady=14)

    def show_logarithm(self):
        self.header_label.config(text="Logarytmy")
        self.clear_content()
        value_entry = self.create_entry("Liczba dodatnia:", 0)
        base_entry = self.create_entry("Podstawa (np. 10 lub e):", 1, "e")

        def calculate():
            try:
                value = float(value_entry.get())
                base_text = base_entry.get().strip().lower()
                base = math.e if base_text in ("e", "2.71828") else float(base_text)
                result = log(value, base)
                self.show_output(f"Logarytm: {result}")
            except ValueError as error:
                messagebox.showerror("Błąd", str(error))
            except Exception:
                messagebox.showerror("Błąd", "Wprowadź poprawne dane.")

        tk.Button(self.content_area, text="Oblicz", command=calculate, width=20).grid(row=2, column=0, columnspan=2, pady=14)

    def show_statistics(self):
        self.header_label.config(text="Statystyka")
        self.clear_content()
        tk.Label(self.content_area, text="Liczby oddzielone spacjami lub przecinkami:").grid(row=0, column=0, columnspan=2, sticky="w", pady=4)
        values_entry = tk.Entry(self.content_area, width=60)
        values_entry.grid(row=1, column=0, columnspan=2, pady=4)

        def calculate():
            text = values_entry.get().replace(",", " ")
            try:
                values = [float(item) for item in text.split() if item]
                if not values:
                    raise ValueError
                results = [
                    f"Średnia: {average(values)}",
                    f"Mediana: {median(values)}",
                    f"Dominanta: {', '.join(str(item) for item in mode(values))}",
                    f"Odchylenie standardowe: {standard_deviation(values)}",
                ]
                self.show_output("\n".join(results))
            except ValueError:
                messagebox.showerror("Błąd", "Wprowadź co najmniej jedną poprawną liczbę.")

        tk.Button(self.content_area, text="Oblicz", command=calculate, width=20).grid(row=2, column=0, columnspan=2, pady=14)

    def show_number_theory(self):
        self.header_label.config(text="Teoria liczb")
        self.clear_content()
        number_entry = self.create_entry("Liczba całkowita:", 0)
        gcd_entry = self.create_entry("Druga liczba do NWD:", 1)

        def calculate():
            try:
                number = int(number_entry.get())
                gcd_number = int(gcd_entry.get())
            except ValueError:
                messagebox.showerror("Błąd", "Wprowadź poprawne liczby całkowite.")
                return
            results = [
                f"Czy pierwsza: {is_prime(number)}",
                f"NWD: {gcd(number, gcd_number)}",
                f"Czynniki pierwsze: {', '.join(str(item) for item in prime_factors(number))}",
            ]
            self.show_output("\n".join(results))

        tk.Button(self.content_area, text="Oblicz", command=calculate, width=20).grid(row=2, column=0, columnspan=2, pady=14)

    def show_geometry(self):
        self.header_label.config(text="Geometria")
        self.clear_content()
        tk.Label(self.content_area, text="Wybierz figurę:").grid(row=0, column=0, sticky="w", pady=4)
        shape_var = tk.StringVar(value="circle")

        def build_inputs():
            for widget in self.content_area.grid_slaves(row=2):
                widget.destroy()
            for widget in self.content_area.grid_slaves(row=3):
                widget.destroy()

            shape = shape_var.get()
            if shape == "circle":
                self.create_entry("Promień:", 2)
            elif shape == "rectangle":
                self.create_entry("Szerokość:", 2)
                self.create_entry("Wysokość:", 3)
            else:
                self.create_entry("Podstawa:", 2)
                self.create_entry("Wysokość:", 3)

        tk.OptionMenu(self.content_area, shape_var, "circle", "rectangle", "triangle", command=lambda _: build_inputs()).grid(row=0, column=1, sticky="w")
        build_inputs()

        def calculate():
            shape = shape_var.get()
            try:
                if shape == "circle":
                    radius = float(self.content_area.grid_slaves(row=2, column=1)[0].get())
                    result = area_circle(radius)
                    self.show_output(f"Pole koła: {result}")
                elif shape == "rectangle":
                    width = float(self.content_area.grid_slaves(row=2, column=1)[0].get())
                    height = float(self.content_area.grid_slaves(row=3, column=1)[0].get())
                    self.show_output(f"Pole prostokąta: {area_rectangle(width, height)}")
                else:
                    base = float(self.content_area.grid_slaves(row=2, column=1)[0].get())
                    height = float(self.content_area.grid_slaves(row=3, column=1)[0].get())
                    self.show_output(f"Pole trójkąta: {area_triangle(base, height)}")
            except Exception:
                messagebox.showerror("Błąd", "Wprowadź poprawne dane.")

        tk.Button(self.content_area, text="Oblicz", command=calculate, width=20).grid(row=4, column=0, columnspan=2, pady=14)

    def show_quadratic(self):
        self.header_label.config(text="Równanie kwadratowe")
        self.clear_content()
        a_entry = self.create_entry("Współczynnik a:", 0)
        b_entry = self.create_entry("Współczynnik b:", 1)
        c_entry = self.create_entry("Współczynnik c:", 2)

        def calculate():
            try:
                a = float(a_entry.get())
                b = float(b_entry.get())
                c = float(c_entry.get())
                roots = solve_quadratic(a, b, c)
                self.show_output(f"Pierwiastki: {roots[0]}, {roots[1]}")
            except ValueError as error:
                messagebox.showerror("Błąd", str(error))
            except Exception:
                messagebox.showerror("Błąd", "Wprowadź poprawne dane.")

        tk.Button(self.content_area, text="Oblicz", command=calculate, width=20).grid(row=3, column=0, columnspan=2, pady=14)


if __name__ == "__main__":
    app = CalculatorGUI()
    app.mainloop()

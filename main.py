import os
import sys

MODULE_ROOT = os.path.dirname(__file__)
sys.path.insert(0, MODULE_ROOT)

from src.logic.calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    root,
    factorial,
    gcd,
    lcm,
    is_prime,
    prime_factors,
    solve_quadratic,
    to_radians,
    to_degrees,
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


def prompt_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Niepoprawna liczba. Spróbuj ponownie.")


def prompt_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Niepoprawna liczba całkowita. Spróbuj ponownie.")


def prompt_list(prompt: str) -> list[float]:
    while True:
        text = input(prompt).strip()
        try:
            values = [float(part) for part in text.replace(",", " ").split() if part]
            if not values:
                raise ValueError
            return values
        except ValueError:
            print("Wprowadź listę liczb oddzielonych spacjami lub przecinkami.")


def print_result(name: str, value) -> None:
    print(f"{name}: {value}")


def main() -> None:
    print("=== Kalkulator matematyczny ===")
    print("Wybierz kategorię obliczeń:")

    categories = [
        ("1", "Podstawowe działania arytmetyczne"),
        ("2", "Potęgi i pierwiastki"),
        ("3", "Trygonometria"),
        ("4", "Logarytmy"),
        ("5", "Statystyka"),
        ("6", "Liczby i teoria liczb"),
        ("7", "Geometria"),
        ("8", "Równanie kwadratowe"),
        ("q", "Zakończ"),
    ]

    while True:
        for key, name in categories:
            print(f"{key}. {name}")

        choice = input("Wybierz opcję: ").strip().lower()
        if choice == "q":
            print("Do zobaczenia!")
            break

        if choice == "1":
            x = prompt_float("Podaj pierwszą liczbę: ")
            y = prompt_float("Podaj drugą liczbę: ")
            print_result("Dodawanie", add(x, y))
            print_result("Odejmowanie", subtract(x, y))
            print_result("Mnożenie", multiply(x, y))
            try:
                print_result("Dzielenie", divide(x, y))
            except ValueError as error:
                print(error)

        elif choice == "2":
            base = prompt_float("Podaj podstawę: ")
            exponent = prompt_float("Podaj wykładnik: ")
            print_result("Potęga", power(base, exponent))
            value = prompt_float("Podaj liczbę do pierwiastkowania: ")
            degree = prompt_float("Podaj stopień pierwiastka (domyślnie 2): ")
            print_result("Pierwiastek", root(value, degree))

        elif choice == "3":
            angle = prompt_float("Podaj miarę kąta w stopniach: ")
            print_result("sin", sin(angle))
            print_result("cos", cos(angle))
            print_result("tan", tan(angle))
            print_result("radiany", to_radians(angle))

        elif choice == "4":
            value = prompt_float("Podaj liczbę dodatnią: ")
            base = prompt_float("Podaj podstawę logarytmu (domyślnie e=2.71828): ")
            print_result("Logarytm", log(value, base))

        elif choice == "5":
            values = prompt_list("Podaj liczby oddzielone spacjami lub przecinkami: ")
            print_result("Średnia", average(values))
            print_result("Mediana", median(values))
            print_result("Dominanta", mode(values))
            print_result("Odchylenie standardowe", standard_deviation(values))

        elif choice == "6":
            value = prompt_int("Podaj liczbę całkowitą: ")
            print_result("Czy pierwsza", is_prime(value))
            print_result(
                "NWD z 1..10", gcd(value, prompt_int("Podaj drugą liczbę całkowitą: "))
            )
            print_result("Czynniki pierwsze", prime_factors(value))

        elif choice == "7":
            print("1. Pole koła\n2. Pole prostokąta\n3. Pole trójkąta")
            shape = input("Wybierz figurę: ").strip()
            if shape == "1":
                radius = prompt_float("Promień: ")
                print_result("Pole koła", area_circle(radius))
            elif shape == "2":
                width = prompt_float("Szerokość: ")
                height = prompt_float("Wysokość: ")
                print_result("Pole prostokąta", area_rectangle(width, height))
            elif shape == "3":
                base = prompt_float("Podstawa: ")
                height = prompt_float("Wysokość: ")
                print_result("Pole trójkąta", area_triangle(base, height))
            else:
                print("Nieznana figura.")

        elif choice == "8":
            a = prompt_float("Podaj współczynnik a: ")
            b = prompt_float("Podaj współczynnik b: ")
            c = prompt_float("Podaj współczynnik c: ")
            roots = solve_quadratic(a, b, c)
            print_result("Pierwiastki równania", roots)

        else:
            print("Nieznana opcja. Spróbuj ponownie.")


if __name__ == "__main__":
    main()

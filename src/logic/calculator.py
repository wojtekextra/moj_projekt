import math
from typing import Iterable, List, Tuple, Union

__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "power",
    "root",
    "factorial",
    "gcd",
    "lcm",
    "is_prime",
    "prime_factors",
    "solve_quadratic",
    "to_radians",
    "to_degrees",
    "sin",
    "cos",
    "tan",
    "log",
    "average",
    "median",
    "mode",
    "standard_deviation",
    "area_circle",
    "area_rectangle",
    "area_triangle",
]


def add(x: float, y: float) -> float:
    return x + y


def subtract(x: float, y: float) -> float:
    return x - y


def multiply(x: float, y: float) -> float:
    return x * y


def divide(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Dzielenie przez zero jest niedozwolone.")
    return x / y


def power(base: float, exponent: float) -> float:
    return math.pow(base, exponent)


def root(value: float, degree: float = 2.0) -> float:
    if degree == 0:
        raise ValueError("Stopień pierwiastka nie może być zerem.")
    if value < 0 and degree % 2 == 0:
        raise ValueError("Nie można obliczyć parzystego pierwiastka z liczby ujemnej.")
    return (
        math.copysign(abs(value) ** (1.0 / degree), value)
        if value < 0
        else value ** (1.0 / degree)
    )


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError(
            "Silnia jest zdefiniowana tylko dla liczb całkowitych nieujemnych."
        )
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def gcd(x: int, y: int) -> int:
    return math.gcd(x, y)


def lcm(x: int, y: int) -> int:
    if x == 0 or y == 0:
        return 0
    return abs(x * y) // gcd(x, y)


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_factors(n: int) -> List[int]:
    value = abs(n)
    factors: List[int] = []
    while value % 2 == 0 and value > 0:
        factors.append(2)
        value //= 2
    divisor = 3
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors.append(divisor)
            value //= divisor
        divisor += 2
    if value > 1:
        factors.append(value)
    return factors


def solve_quadratic(a: float, b: float, c: float) -> Tuple[Union[float, complex], ...]:
    if a == 0:
        raise ValueError("Współczynnik a nie może być zerem w równaniu kwadratowym.")
    delta = b * b - 4 * a * c
    if delta < 0:
        return tuple(
            sorted(
                ((-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a))
            )
        )
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)
    return (root1, root2) if root1 <= root2 else (root2, root1)


def to_radians(degrees: float) -> float:
    return math.radians(degrees)


def to_degrees(radians: float) -> float:
    return math.degrees(radians)


def sin(degrees: float) -> float:
    return math.sin(to_radians(degrees))


def cos(degrees: float) -> float:
    return math.cos(to_radians(degrees))


def tan(degrees: float) -> float:
    return math.tan(to_radians(degrees))


def log(value: float, base: float = math.e) -> float:
    if value <= 0:
        raise ValueError("Logarytm jest zdefiniowany tylko dla liczb dodatnich.")
    if base <= 0 or base == 1:
        raise ValueError("Podstawa logarytmu musi być dodatnia i różna od 1.")
    return math.log(value, base)


def _validate_numeric_list(values: Iterable[float]) -> List[float]:
    numbers = list(values)
    if not numbers:
        raise ValueError("Lista wartości nie może być pusta.")
    return numbers


def average(values: Iterable[float]) -> float:
    numbers = _validate_numeric_list(values)
    return sum(numbers) / len(numbers)


def median(values: Iterable[float]) -> float:
    numbers = sorted(_validate_numeric_list(values))
    n = len(numbers)
    mid = n // 2
    return numbers[mid] if n % 2 == 1 else (numbers[mid - 1] + numbers[mid]) / 2


def mode(values: Iterable[float]) -> List[float]:
    numbers = _validate_numeric_list(values)
    counts = {}
    for value in numbers:
        counts[value] = counts.get(value, 0) + 1
    max_count = max(counts.values())
    return sorted([value for value, count in counts.items() if count == max_count])


def standard_deviation(values: Iterable[float]) -> float:
    numbers = _validate_numeric_list(values)
    mean_value = average(numbers)
    variance = sum((x - mean_value) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)


def area_circle(radius: float) -> float:
    if radius < 0:
        raise ValueError("Promień nie może być ujemny.")
    return math.pi * radius * radius


def area_rectangle(width: float, height: float) -> float:
    if width < 0 or height < 0:
        raise ValueError("Wymiary prostokąta muszą być nieujemne.")
    return width * height


def area_triangle(base: float, height: float) -> float:
    if base < 0 or height < 0:
        raise ValueError("Wymiary trójkąta muszą być nieujemne.")
    return 0.5 * base * height

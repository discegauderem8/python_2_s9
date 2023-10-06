import math

def find_roots_decorator(func):
    def wrapper(a, b, c, *extra):
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            print(f"Корень 1: {root1}")
            print(f"Корень 2: {root2}")
        elif discriminant == 0:
            root = -b / (2*a)
            print(f"Единственный корень: {root}")
        else:
            print("Корни квадратного уравнения отсутствуют (дискриминант меньше нуля)")

        return func(a, b, c)
    return wrapper

@find_roots_decorator
def solve_equation(a, b, c):
    pass  # В этой функции мы не будем делать ничего, так как декоратор выводит результат


solve_equation(1, -3, 2)

import csv
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

def process_csv_decorator(filename):
    def decorator(func):
        def wrapper():
            with open(filename, newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    if len(row) == 3:
                        a, b, c = map(int, row)
                        func(a, b, c)
                    else:
                        print("Некорректное количество чисел в строке CSV файла.")
        return wrapper
    return decorator

@process_csv_decorator("random_data.csv")
@find_roots_decorator
def solve_equation(a, b, c):
    pass

solve_equation()


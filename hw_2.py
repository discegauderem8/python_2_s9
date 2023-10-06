import csv
import random


def generate_csv_decorator(min_rows=100, max_rows=1000):
    def decorator(func):
        def wrapper(filename):
            num_rows = random.randint(min_rows, max_rows)
            with open(filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                for _ in range(num_rows):
                    row = [random.randint(1, 1000) for _ in range(3)]
                    csv_writer.writerow(row)
            print(f"Сгенерирован CSV файл '{filename}' с {num_rows} строками.")
            return func(filename)
        return wrapper
    return decorator

@generate_csv_decorator()
def process_csv(filename):
    pass

process_csv("random_data.csv")

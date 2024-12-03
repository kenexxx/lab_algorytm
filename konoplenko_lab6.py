import random
import time

# Реалізація алгоритму Merge
def merge(B, C, A):
    i, j, k = 0, 0, 0
    p, q = len(B), len(C)
    while i < p and j < q:
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1
    while i < p:
        A[k] = B[i]
        i += 1
        k += 1
    while j < q:
        A[k] = C[j]
        j += 1
        k += 1

# Реалізація алгоритму Mergesort
def mergesort(A):
    n = len(A)
    if n > 1:
        mid = n // 2
        B = A[:mid]
        C = A[mid:]
        mergesort(B)
        mergesort(C)
        merge(B, C, A)

# Генерація випадкової послідовності
def generate_random_sequence(size, min_val=0, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]

# Збереження списку у файл
def save_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write(' '.join(map(str, data)))

# Зчитування списку з файлу
def load_from_file(filename):
    with open(filename, 'r') as f:
        return list(map(int, f.read().split()))

# Вимірювання часу виконання алгоритму
def measure_time(sort_function, data):
    start_time = time.time()
    sort_function(data)
    end_time = time.time()
    return end_time - start_time

# Інтерфейс користувача
def main():
    print("Лабораторна робота: Сортування злиттям (Mergesort)")

    size = int(input("Введіть розмір випадкової послідовності: "))
    random_sequence = generate_random_sequence(size)
    print(f"\nЗгенерована послідовність: {random_sequence}")

    input_filename = "random_sequence.txt"
    output_filename = "sorted_sequence.txt"
    save_to_file(input_filename, random_sequence)
    print(f"\nПослідовність збережено у файл: {input_filename}")

    # Сортування злиттям
    sorted_sequence = random_sequence.copy()
    sorting_time = measure_time(mergesort, sorted_sequence)
    save_to_file(output_filename, sorted_sequence)
    print(f"\nВідсортована послідовність: {sorted_sequence}")
    print(f"Час сортування: {sorting_time:.6f} секунд")
    print(f"Відсортована послідовність збережена у файл: {output_filename}")

if __name__ == "__main__":
    main()



import random
import time

# Реалізація алгоритмів сортування
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Генерація випадкової послідовності
def generate_random_sequence(size, max_value=1000):
    return [random.randint(0, max_value) for _ in range(size)]

# Запис у файл
def write_to_file(filename, data):
    with open(filename, "w") as file:
        file.write(" ".join(map(str, data)))

# Зчитування з файлу
def read_from_file(filename):
    with open(filename, "r") as file:
        return list(map(int, file.read().split()))

# Вимірювання часу виконання
def measure_execution_time(sort_function, arr):
    start_time = time.time()
    sorted_arr = sort_function(arr.copy())
    end_time = time.time()
    return sorted_arr, end_time - start_time

# Інтерфейс користувача
def user_interface():
    print("Введіть обсяг випадкової послідовності:")
    size = int(input())
    max_value = int(input("Введіть максимальне значення елементів: "))
    
    random_sequence = generate_random_sequence(size, max_value)
    print(f"Згенерована послідовність: {random_sequence}")
    write_to_file("random_sequence.txt", random_sequence)
    print("Послідовність збережено у файл random_sequence.txt")

    algorithms = {
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Heap Sort": heap_sort,
        "Quick Sort": quick_sort,
    }

    print("\nВиконується сортування різними алгоритмами...")
    results = {}
    for name, algorithm in algorithms.items():
        sorted_arr, exec_time = measure_execution_time(algorithm, random_sequence)
        results[name] = (sorted_arr, exec_time)
        write_to_file(f"sorted_sequence_{name.replace(' ', '_')}.txt", sorted_arr)
        print(f"{name}: час виконання {exec_time:.6f} секунд")
        print(f"Відсортована послідовність збережена у файл sorted_sequence_{name.replace(' ', '_')}.txt")

    print("\nПорівняння:")
    for name, (sorted_arr, exec_time) in results.items():
        print(f"{name}: час виконання {exec_time:.6f} секунд")

# Головна функція
def main():
    print("1. Реалізувати алгоритм QuickSort")
    print("2. Провести порівняльний аналіз")
    print("3. Запустити інтерфейс користувача")
    
    choice = int(input("Оберіть дію (1/2/3): "))
    if choice == 1:
        print("Алгоритм QuickSort реалізовано.")
    elif choice == 2:
        size = int(input("Введіть розмір послідовності для порівняння: "))
        random_sequence = generate_random_sequence(size)

        algorithms = {
            "Insertion Sort": insertion_sort,
            "Merge Sort": merge_sort,
            "Heap Sort": heap_sort,
            "Quick Sort": quick_sort,
        }

        print("\nПорівняння алгоритмів сортування:")
        for name, algorithm in algorithms.items():
            _, exec_time = measure_execution_time(algorithm, random_sequence)
            print(f"{name}: час виконання {exec_time:.6f} секунд")
    elif choice == 3:
        user_interface()
    else:
        print("Невірний вибір!")

# Запуск програми
if __name__ == "__main__":
    main()


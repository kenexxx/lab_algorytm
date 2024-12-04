import random
import time

# Алгоритм InsertionSort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Алгоритм MergeSort
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

# Генерація випадкової послідовності
def generate_random_sequence(size):
    return [random.randint(0, 10000) for _ in range(size)]

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
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Основний інтерфейс користувача
def main():
    print("Вітаємо! Введіть розмір випадкової послідовності:")
    size = int(input())
    array = generate_random_sequence(size)

    print("Генерується випадкова послідовність...")
    write_to_file("random_sequence.txt", array)
    print("Послідовність збережено у файл random_sequence.txt.")

    sorted_array_insertion = insertion_sort(array.copy())
    write_to_file("sorted_sequence_insertion.txt", sorted_array_insertion)
    print("Відсортована послідовність (InsertionSort) збережена у файл sorted_sequence_insertion.txt.")

    sorted_array_merge = merge_sort(array.copy())
    write_to_file("sorted_sequence_merge.txt", sorted_array_merge)
    print("Відсортована послідовність (MergeSort) збережена у файл sorted_sequence_merge.txt.")

    print("Порівняльний аналіз алгоритмів...")
    time_insertion = measure_execution_time(insertion_sort, array.copy())
    time_merge = measure_execution_time(merge_sort, array.copy())

    print(f"Час виконання InsertionSort: {time_insertion:.5f} секунд")
    print(f"Час виконання MergeSort: {time_merge:.5f} секунд")

# Запуск програми
if __name__ == "__main__":
    main()


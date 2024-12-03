import random
import time

# Алгоритм S (послідовний пошук)
def sequential_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i  # Повертаємо позицію
    return -1  # Якщо елемент не знайдений

# Алгоритм Q (швидкий послідовний пошук)
def quick_sequential_search(arr, key):
    n = len(arr)
    arr.append(key)  # Додаємо "сторожовий" елемент
    i = 0
    while arr[i] != key:
        i += 1
    arr.pop()  # Видаляємо "сторожовий" елемент
    return i if i < n else -1  # Перевіряємо, чи елемент у межах списку

# Генерація випадкової послідовності
def generate_random_sequence(size, min_val=0, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]

# Вивід елемента для перевірки
def get_element_by_position(arr, pos):
    if 0 <= pos < len(arr):
        return arr[pos]
    return None

# Вимірювання часу виконання алгоритмів
def measure_time(search_function, arr, key):
    start_time = time.time()
    position = search_function(arr, key)
    end_time = time.time()
    return position, end_time - start_time

# Порівняння алгоритмів
def compare_algorithms(size, key):
    arr = generate_random_sequence(size)
    print(f"Генерована послідовність: {arr}")
    
    # Алгоритм S
    pos_s, time_s = measure_time(sequential_search, arr, key)
    print(f"Алгоритм S: Позиція = {pos_s}, Час = {time_s:.6f} секунд")
    
    # Алгоритм Q
    pos_q, time_q = measure_time(quick_sequential_search, arr, key)
    print(f"Алгоритм Q: Позиція = {pos_q}, Час = {time_q:.6f} секунд")

# Інтерфейс користувача
def main():
    print("Лабораторна робота: Порівняння алгоритмів пошуку (S і Q)")

    size = int(input("Введіть обсяг випадкової послідовності: "))
    key = int(input("Введіть аргумент пошуку (ключ): "))

    arr = generate_random_sequence(size)
    print("\nВипадкова послідовність згенерована.")
    print("Для перевірки можна вивести елемент за певною позицією.")

    while True:
        print("\nОперації:")
        print("1. Знайти позицію елемента алгоритмом S")
        print("2. Знайти позицію елемента алгоритмом Q")
        print("3. Вивести елемент за позицією")
        print("4. Порівняти ефективність алгоритмів")
        print("5. Вийти")
        choice = int(input("Ваш вибір: "))

        if choice == 1:
            pos = sequential_search(arr, key)
            print(f"Позиція елемента: {pos}" if pos != -1 else "Елемент не знайдений.")
        elif choice == 2:
            pos = quick_sequential_search(arr, key)
            print(f"Позиція елемента: {pos}" if pos != -1 else "Елемент не знайдений.")
        elif choice == 3:
            pos = int(input("Введіть позицію елемента: "))
            elem = get_element_by_position(arr, pos)
            print(f"Елемент на позиції {pos}: {elem}" if elem is not None else "Невірна позиція.")
        elif choice == 4:
            compare_algorithms(size, key)
        elif choice == 5:
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()



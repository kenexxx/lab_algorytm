import random
import time

# Алгоритм грубої сили (Intersect_bruteforce)
def intersect_bruteforce(A, B):
    intersection = []
    iterations = 0
    for a in A:
        for b in B:
            iterations += 1
            if a == b:
                intersection.append(a)
                break
    return intersection, iterations

# Алгоритм із використанням сортування (Intersect_conversion)
def intersect_conversion(A, B):
    A.sort()
    B.sort()
    intersection = []
    i = j = iterations = 0

    while i < len(A) and j < len(B):
        iterations += 1
        if A[i] == B[j]:
            intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1

    return intersection, iterations

# Генерація множин
def generate_random_set(size, range_max=1000):
    return [random.randint(1, range_max) for _ in range(size)]

# Виведення множини
def display_set(name, data):
    print(f"{name}: {data}")

# Вимірювання часу виконання
def measure_execution_time(func, *args):
    start_time = time.time()
    result, iterations = func(*args)
    end_time = time.time()
    return result, end_time - start_time, iterations

# Основний інтерфейс користувача
def main():
    print("Вітаємо! Введіть обсяг множин (або 0 для автоматичної генерації):")
    size = int(input())

    if size > 0:
        print("Введіть елементи множини A через пробіл:")
        A = list(map(int, input().split()))
        print("Введіть елементи множини B через пробіл:")
        B = list(map(int, input().split()))
    else:
        size = int(input("Введіть бажаний розмір множин для автоматичної генерації: "))
        A = generate_random_set(size)
        B = generate_random_set(size)
        print("Множини згенеровано випадковим чином.")

    display_set("Множина A", A)
    display_set("Множина B", B)

    print("\nОбчислення перетину за допомогою Intersect_bruteforce...")
    intersection_bf, time_bf, iterations_bf = measure_execution_time(intersect_bruteforce, A, B)
    display_set("Перетин (Intersect_bruteforce)", intersection_bf)
    print(f"Час виконання: {time_bf:.6f} секунд, Кількість ітерацій: {iterations_bf}")

    print("\nОбчислення перетину за допомогою Intersect_conversion...")
    intersection_conv, time_conv, iterations_conv = measure_execution_time(intersect_conversion, A, B)
    display_set("Перетин (Intersect_conversion)", intersection_conv)
    print(f"Час виконання: {time_conv:.6f} секунд, Кількість ітерацій: {iterations_conv}")

    print("\nПорівняння:")
    print(f"Intersect_bruteforce: Час = {time_bf:.6f} секунд, Ітерації = {iterations_bf}")
    print(f"Intersect_conversion: Час = {time_conv:.6f} секунд, Ітерації = {iterations_conv}")

# Запуск програми
if __name__ == "__main__":
    main()

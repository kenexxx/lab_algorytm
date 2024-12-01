import time
import matplotlib.pyplot as plt
import pandas as pd

# 1. Реалізація рекурсивного алгоритму розв’язання задачі про ханойські вежі
def hanoi_recursive(n, source, target, auxiliary):
    """
    Рекурсивний алгоритм розв’язання задачі про ханойські вежі.
    """
    steps = []
    def solve(n, source, target, auxiliary):
        if n == 1:
            steps.append(f"Перемістити диск із кілочка №{source} на кілочок №{target}")
            return
        solve(n - 1, source, auxiliary, target)
        steps.append(f"Перемістити диск із кілочка №{source} на кілочок №{target}")
        solve(n - 1, auxiliary, target, source)
    solve(n, source, target, auxiliary)
    return steps

# 2. Математичний аналіз: кількість переміщень
def hanoi_moves_count(n):
    return 2 ** n - 1

# 3. Емпіричний аналіз
def empirical_analysis(max_disks):
    results = []
    for n in range(1, max_disks + 1):
        start_time = time.time()
        steps = hanoi_recursive(n, 1, 3, 2)
        end_time = time.time()
        elapsed_time = end_time - start_time
        results.append((n, elapsed_time, len(steps)))
    return results

# 4. Побудова графіка
def plot_analysis(results):
    n_values = [result[0] for result in results]
    times = [result[1] for result in results]

    plt.scatter(n_values, times, label="Час виконання", color='blue')
    plt.xlabel("Кількість дисків")
    plt.ylabel("Час виконання (секунди)")
    plt.title("Залежність часу виконання від кількості дисків")
    plt.legend()
    plt.grid()
    plt.show()

# 5. Інтерфейс користувача
def user_interface():
    """
    Інтерактивна функція для введення кількості дисків та виведення послідовності дій.
    """
    try:
        n = int(input("Введіть кількість дисків (n): "))
        if n < 1:
            print("Кількість дисків має бути позитивним числом.")
            return

        steps = hanoi_recursive(n, 1, 3, 2)
        print(f"Послідовність дій для {n} дисків:")
        for step in steps:
            print(step)
    except ValueError:
        print("Будь ласка, введіть ціле число.")

# Проведення емпіричного аналізу
max_disks = 10
results = empirical_analysis(max_disks)

# Виведення таблиці результатів
df = pd.DataFrame(results, columns=["Кількість дисків", "Час виконання (с)", "Кількість кроків"])
print(df)

# Побудова графіка залежності часу роботи алгоритму
plot_analysis(results)

# Інтерфейс користувача
user_interface()

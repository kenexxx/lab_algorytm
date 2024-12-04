import random
import time

# Алгоритм обчислення перетину множин (груба сила)
def intersection_bruteforce(A, B):
    intersection = []
    for a in A:
        if a in B:
            intersection.append(a)
    return intersection

# Функція тестування алгоритму
def test_algorithm():
    print("\nТестування алгоритму:")
    
    # Тест 1
    A = [1, 2, 3, 4]
    B = [3, 4, 5, 6]
    expected = [3, 4]
    result = intersection_bruteforce(A, B)
    print(f"Тест 1: {'Успішно' if result == expected else 'Помилка'}, Результат: {result}, Очікувано: {expected}")
    
    # Тест 2
    A = [10, 20, 30]
    B = [40, 50, 60]
    expected = []
    result = intersection_bruteforce(A, B)
    print(f"Тест 2: {'Успішно' if result == expected else 'Помилка'}, Результат: {result}, Очікувано: {expected}")
    
    # Тест 3
    A = [1, 2, 3, 4]
    B = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]
    result = intersection_bruteforce(A, B)
    print(f"Тест 3: {'Успішно' if result == expected else 'Помилка'}, Результат: {result}, Очікувано: {expected}")

# Генерація випадкових множин
def generate_random_set(size, max_value=100):
    return [random.randint(1, max_value) for _ in range(size)]

# Інтерфейс користувача
def user_interface():
    print("\nІнтерфейс користувача")
    print("1. Ручний ввід множин")
    print("2. Автоматична генерація множин")
    choice = int(input("Виберіть опцію (1/2): "))
    
    if choice == 1:
        print("Введіть елементи множини A через пробіл:")
        A = list(map(int, input().split()))
        print("Введіть елементи множини B через пробіл:")
        B = list(map(int, input().split()))
    elif choice == 2:
        size = int(input("Введіть розмір множин: "))
        max_value = int(input("Введіть максимальне значення елементів множин: "))
        A = generate_random_set(size, max_value)
        B = generate_random_set(size, max_value)
        print("Множини згенеровано випадковим чином.")
    else:
        print("Невірний вибір!")
        return
    
    print(f"Множина A: {A}")
    print(f"Множина B: {B}")
    
    print("\nОбчислення перетину множин...")
    start_time = time.time()
    result = intersection_bruteforce(A, B)
    end_time = time.time()
    
    print(f"Перетин множин: {result}")
    print(f"Час виконання: {end_time - start_time:.6f} секунд")

# Головна функція
def main():
    print("Меню:")
    print("1. Реалізувати алгоритм")
    print("2. Протестувати алгоритм")
    print("3. Виконати програму з інтерфейсом користувача")
    
    choice = int(input("Виберіть опцію (1/2/3): "))
    
    if choice == 1:
        print("Алгоритм реалізовано. Використовуйте інші функції для перевірки.")
    elif choice == 2:
        test_algorithm()
    elif choice == 3:
        user_interface()
    else:
        print("Невірний вибір!")

# Запуск програми
if __name__ == "__main__":
    main()

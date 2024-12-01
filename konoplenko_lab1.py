def gcd_euclid(m, n):
    """
    Реалізація алгоритму Евкліда для обчислення НСД.
    """
    while n != 0:
        m, n = n, m % n
    return m


def gcd_sequential(m, n):
    """
    Реалізація алгоритму послідовного перебору для обчислення НСД.
    """
    t = min(m, n)
    while t > 0:
        if m % t == 0 and n % t == 0:
            return t
        t -= 1


def test_algorithms():
    """
    Тестування алгоритмів на різних прикладах.
    """
    test_cases = [(48, 18), (56, 42), (101, 103), (100, 75)]
    for m, n in test_cases:
        euclid_result = gcd_euclid(m, n)
        sequential_result = gcd_sequential(m, n)
        print(f"Числа: {m}, {n}")
        print(f"НСД за алгоритмом Евкліда: {euclid_result}")
        print(f"НСД за методом послідовного перебору: {sequential_result}")
        print("-" * 50)


def user_interface():
    """
    Інтерфейс користувача для введення чисел і вибору методу обчислення НСД.
    """
    print("Обчислення НСД двох чисел")
    while True:
        try:
            m = int(input("Введіть перше число (m): "))
            n = int(input("Введіть друге число (n): "))
        except ValueError:
            print("Будь ласка, введіть цілі числа.")
            continue

        print("Оберіть метод:")
        print("1. Алгоритм Евкліда")
        print("2. Метод послідовного перебору")
        print("3. Вихід")
        choice = input("Ваш вибір: ")

        if choice == "1":
            result = gcd_euclid(m, n)
            print(f"НСД за алгоритмом Евкліда: {result}")
        elif choice == "2":
            result = gcd_sequential(m, n)
            print(f"НСД за методом послідовного перебору: {result}")
        elif choice == "3":
            print("До побачення!")
            break
        else:
            print("Некоректний вибір, спробуйте ще раз.")

        print("-" * 50)


if __name__ == "__main__":
    # Тестування алгоритмів
    test_algorithms()

    # Запуск інтерфейсу користувача
    user_interface()

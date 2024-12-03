class LinearList:
    def __init__(self):
        self.data = []

    def insert(self, x, p):
        if 0 <= p <= len(self.data):
            self.data.insert(p, x)
        else:
            raise IndexError("Invalid position")

    def locate(self, x):
        try:
            return self.data.index(x)
        except ValueError:
            return -1

    def retrieve(self, p):
        if 0 <= p < len(self.data):
            return self.data[p]
        else:
            raise IndexError("Invalid position")

    def delete(self, p):
        if 0 <= p < len(self.data):
            del self.data[p]
        else:
            raise IndexError("Invalid position")

    def next(self, p):
        if 0 <= p < len(self.data) - 1:
            return p + 1
        else:
            return -1

    def previous(self, p):
        if 0 < p < len(self.data):
            return p - 1
        else:
            return -1

    def makenull(self):
        self.data = []

    def first(self):
        return 0 if len(self.data) > 0 else -1

    def printlist(self):
        print(" -> ".join(map(str, self.data)) if self.data else "Empty list")

class Stack:
    def __init__(self):
        self.data = []

    def makenull(self):
        self.data = []

    def top(self):
        if self.data:
            return self.data[-1]
        else:
            raise IndexError("Stack is empty")

    def pop(self):
        if self.data:
            return self.data.pop()
        else:
            raise IndexError("Stack is empty")

    def push(self, x):
        self.data.append(x)

    def empty(self):
        return len(self.data) == 0

def is_palindrome(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_s = ""
    while not stack.empty():
        reversed_s += stack.pop()
    
    return s == reversed_s

def main():
    print("Лабораторна робота: АТД лінійний список та стек")

    # Лінійний список
    print("\n1. Робота з лінійним списком")
    lst = LinearList()
    n = int(input("Введіть кількість елементів у списку: "))
    for i in range(n):
        elem = input(f"Введіть елемент {i+1}: ")
        lst.insert(elem, i)

    while True:
        print("\nОперації над списком:")
        print("1. Вставка елемента")
        print("2. Знайти позицію елемента")
        print("3. Отримати елемент за позицією")
        print("4. Видалити елемент за позицією")
        print("5. Вивести список")
        print("6. Зробити список порожнім")
        print("7. Вийти")
        choice = int(input("Ваш вибір: "))

        if choice == 1:
            x = input("Введіть елемент: ")
            p = int(input("Введіть позицію: "))
            lst.insert(x, p)
        elif choice == 2:
            x = input("Введіть елемент: ")
            print("Позиція:", lst.locate(x))
        elif choice == 3:
            p = int(input("Введіть позицію: "))
            print("Елемент:", lst.retrieve(p))
        elif choice == 4:
            p = int(input("Введіть позицію: "))
            lst.delete(p)
        elif choice == 5:
            lst.printlist()
        elif choice == 6:
            lst.makenull()
        elif choice == 7:
            break
        else:
            print("Невірний вибір, спробуйте ще раз!")

    # Перевірка паліндрому
    print("\n2. Перевірка паліндрому")
    s = input("Введіть рядок: ")
    if is_palindrome(s):
        print(f"Рядок '{s}' є паліндромом.")
    else:
        print(f"Рядок '{s}' не є паліндромом.")

if __name__ == "__main__":
    main()


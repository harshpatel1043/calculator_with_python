import operator
from colorama import Fore
class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            print("Error: ")
            return None
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_input(self):
        num1 = input("| enter the first number    |").strip()
        num2 = input("| enter the second number    |").strip()
        operation = input("| enter the operation (+, -, *, /)  |").strip()
        return float(num1), float(num2), operation

    def display_history(self):
        print("\nCalculation History:")
        for i, entry in enumerate(self.history, start=1):
            print(f"{i}. {entry}")

    def run(self):
        while True:
            print(Fore.RED + "welcome to my calculator")
            print(Fore.YELLOW + "+----------------------+")
            print(Fore.YELLOW + "|      1. Add          |")
            print("|    2. Subtract       |")
            print("|    3. Multiply       |")
            print("|    4. Divide         |")
            print("|  5. show history     |")
            print("|  6. Try new input    |")
            print("+----------------------+")
            print(Fore.BLUE + "\n+----------------------+")
            print("|   MADE BY HARSH     |")
            print("+----------------------+")
            print(Fore.CYAN + "\n+---------------------------+")
            choice = input("|    enter your choice      |").strip()
            if choice == '1':
                num1, num2, operation = self.get_input()
                if operation == '+':
                    result = self.add(num1, num2)
                    print("+-------------+")
                    print(Fore.MAGENTA + f"Result: {result}")
                    print("+-------------+")
            elif choice == '2':
                num1, num2, operation = self.get_input()
                if operation == '-':
                    result = self.subtract(num1, num2)
                    print("+-------------+")
                    print(Fore.MAGENTA + f"Result: {result}")
                    print("+-------------+")
            elif choice == '3':
                num1, num2, operation = self.get_input()
                if operation == '*':
                    result = self.multiply(num1, num2)
                    print("+-------------+")
                    print(Fore.MAGENTA + f"Result: {result}")
                    print("+-------------+")
            elif choice == '4':
                num1, num2, operation = self.get_input()
                if operation == '/':
                    result = self.divide(num1, num2)
                    print("+-------------+")
                    print(Fore.MAGENTA + f"Result: {result}")
                    print("+-------------+")
            elif choice == '5':
                self.display_history()
            elif choice == '6':
                print("+-------------+")
                print(Fore.MAGENTA + f"Result: {result}")
                print("+-------------+")
                sys.exit()
            else:
                print("invalid choice. please try again")

if __name__ == "__main__":
    calc = Calculator()
    calc.run()

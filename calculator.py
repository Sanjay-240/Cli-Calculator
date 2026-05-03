# ============================================
# CLI CALCULATOR WITH TIMESTAMP HISTORY
# ============================================

import math
from datetime import datetime

history = []

# ========== OPERATIONS ==========
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero"
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error! Negative number"
    return math.sqrt(a)

# ========== INPUT ==========
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Invalid input! Enter a number.")

# ========== MENU ==========
def show_menu():
    print("\n===== ADVANCED CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Show History")
    print("8. Exit")

# ========== FORMAT ENTRY ==========
def format_entry(expression, result):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{now}] {expression} = {result}"

# ========== SAVE ==========
def save_to_file(entry):
    try:
        with open("history.txt", "a", encoding="utf-8") as file:
            file.write(entry + "\n")
    except Exception as e:
        print("File save error:", e)

# ========== SHOW FILE HISTORY ==========
def show_file_history():
    try:
        print("\n--- Saved History (File) ---")
        with open("history.txt", "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())
    except:
        print("No history file found.")

# ========== MAIN ==========
def main():
    while True:
        show_menu()
        choice = input("Enter choice (1-8): ")

        if choice == '8':
            print("Calculator Closed")
            break

        if choice == '7':
            print("\n--- Session History ---")
            for item in history:
                print(item)
            show_file_history()
            continue

        if choice == '6':
            num = get_number("Enter number: ")
            result = square_root(num)
            expr = f"sqrt({num})"

        else:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                result = add(num1, num2)
                expr = f"{num1} + {num2}"

            elif choice == '2':
                result = sub(num1, num2)
                expr = f"{num1} - {num2}"

            elif choice == '3':
                result = mul(num1, num2)
                expr = f"{num1} * {num2}"

            elif choice == '4':
                result = div(num1, num2)
                expr = f"{num1} / {num2}"

            elif choice == '5':
                result = power(num1, num2)
                expr = f"{num1}^{num2}"

            else:
                print("Invalid choice!")
                continue

        entry = format_entry(expr, result)

        print("Result:", result)

        # Save history
        history.append(entry)
        save_to_file(entry)

# ========== RUN ==========
if __name__ == "__main__":
    main()
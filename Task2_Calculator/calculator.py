def show_menu():
    print("\n============================")
    print("      🧮 PYTHON CALCULATOR  ")
    print("============================")
    print("1️⃣  Addition")
    print("2️⃣  Subtraction")
    print("3️⃣  Multiplication")
    print("4️⃣  Division")
    print("5️⃣  Exit 🚪")
  
def add(a, b):
    return a + b
  
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
  
def divide(a, b):
    if b == 0:
        return "❌ Error: Division by zero is not allowed"
    return a / b

while True:
    show_menu()
    choice = input("👉 Enter your choice (1-5): ")

    if choice == "5":
        print("👋 Thank you for using the calculator!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("⚠️ Invalid choice. Please select a valid option.")
        continue

    try:
        num1 = float(input("🔢 Enter first number: "))
        num2 = float(input("🔢 Enter second number: "))
    except ValueError:
        print("❗ Invalid input! Please enter numeric values.")
        continue

    if choice == "1":
        result = add(num1, num2)
        operation = "Addition "
    elif choice == "2":
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif choice == "3":
        result = multiply(num1, num2)
        operation = "Multiplication"
    elif choice == "4":
        result = divide(num1, num2)
        operation = "Division"
      
    print(f"✅ {operation} \n Result: {result}")

def main():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers!")
        return

    if choice == "1":
        print(f"{x} + {y} = {add(x, y)}")
    elif choice == "2":
        print(f"{x} - {y} = {sub(x, y)}")
    elif choice == "3":
        print(f"{x} * {y} = {multiply(x, y)}")
    elif choice == "4":
        print(f"{x} / {y} = {divide(x, y)}")
    else:
        print(" Invalid choice")

if __name__ == "__main__":
    main()

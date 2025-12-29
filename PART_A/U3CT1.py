print("=== Area Calculator ===")

while True:
    print("\nChoose a shape:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")

    choice = input("Enter your choice (1/2/3): ")

    # Decide which area formula to use
    if choice == "1":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print("Area of Rectangle:", area)

    elif choice == "2":
        radius = float(input("Enter radius: "))
        area = 3.14 * radius * radius
        print("Area of Circle:", area)

    elif choice == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print("Area of Triangle:", area)

    else:
        print("Invalid choice. Please try again.")
        continue

    print("\nCalculation completed!")

    # Exit condition
    again = input("\nDo you want to calculate another area? (yes/no): ").lower()
    if again != "yes":
        print("Program ended.")
        break

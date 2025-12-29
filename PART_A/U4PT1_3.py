# Store user input in variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

# Display stored values
print("\n--- Stored Information ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Simple variable manipulation
age_next_year = age + 1
if age_next_year < 30:
    print("\nNext year, you will be", age_next_year, 
        "years old — still young enough to forget where you left your keys!")
else:
    print("\nNext year, you will be", age_next_year, 
        "years old — welcome to the age where naps become a hobby!")


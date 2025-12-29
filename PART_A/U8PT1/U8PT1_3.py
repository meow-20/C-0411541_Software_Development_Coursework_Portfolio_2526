# 3. Drawing a Recursive Fractal Pattern (Text-Based Example)
def draw_triangle(n):
    if n == 0:  # Base case
        return
    draw_triangle(n - 1)  # Recursive call
    print("*" * n)  # Print stars for current level

# Example usage
levels = int(input("Enter number of levels: "))
print(f"Recursive triangle with {levels} levels:")
draw_triangle(levels)

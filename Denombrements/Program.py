import sys

def factorial(n):
    """Calculates the factorial of a number."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def get_input(prompt):
    """Gets an integer input from the user."""
    return int(input(prompt))

def permutation():
    """Calculates and prints a permutation."""
    n = get_input("Enter the total number of elements: ")
    print(f"{n}! = {factorial(n)}")

def arrangement():
    """Calculates and prints an arrangement.""" 
    total = get_input("Enter the total number of elements: ")
    subset = get_input("Enter the number of elements in the subset: ")
    result = 1
    for i in range(total - subset + 1, total + 1):
        result *= i
    print(f"A({total}/{subset}) = {result}")

def combination():
    """Calculates and prints a combination."""
    total = get_input("Enter the total number of elements: ")
    subset = get_input("Enter the number of elements in the subset: ")
    numerator = 1
    for i in range(total - subset + 1, total + 1):
        numerator *= i
    denominator = factorial(subset)
    print(f"C({total}/{subset}) = {numerator // denominator}")

def main():
    """Main function to display the menu and process user choices."""
    while True:
        print("\nChoose an option:")
        print("1 - Permutation")
        print("2 - Arrangement")
        print("3 - Combination")
        print("0 - Quit")
        
        choice = get_input("Enter your choice: ")
        
        if choice == 0:
            print("Goodbye!")
            sys.exit()
        elif choice == 1:
            permutation()
        elif choice == 2:
            arrangement()
        elif choice == 3:
            combination()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
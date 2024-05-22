#Fully coded by Ahmed ABS, WARNING: if you want to use code for something that you want please give me credits
import math

def show_pi():
    """Function to show the value of pi."""
    print("The value of pi is:", math.pi)

def solve_math_problem():
    """Function to solve any math problem entered by the user."""
    problem = input("Enter the math problem you want to solve: ")
    try:
        result = eval(problem)
        print("Solution:", result)
    except Exception as e:
        print("Error:", e)

def main():
    print("[*] Welcome to the Math Problem Solver!, originaly made by Ahmed ABS!!")
    print("[*] Choose an option:")
    print("[1] Show the value of pi")
    print("[2] Solve any math problem")
    choice = input("[*] Enter your choice (1 of 2): ")

    if choice == '1':
        show_pi()
    elif choice == '2':
        solve_math_problem()
    else:
        print("[*] Error !!!!! invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

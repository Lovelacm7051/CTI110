# Simple Math Quiz

# CTI-110

# Lovelace, Michael

# 12/5/2023


import random

def generate_numbers():
    num1 = random.randint(1, 999)
    num2 = random.randint(1, 999)
    return num1, num2

def add_numbers():
    num1, num2 = generate_numbers()
    correct_answer = num1 + num2
    return num1, num2, correct_answer

def subtract_numbers():
    num1, num2 = generate_numbers()
    correct_answer = abs(num1 - num2)
    return num1, num2, correct_answer

def display_menu():
    print("\nMENU:")
    print("1. Add numbers")
    print("2. Subtract numbers")
    print("3. Quit")

def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            num1, num2, correct_answer = add_numbers()
            play_game(num1, num2, correct_answer, "add")
        elif choice == "2":
            num1, num2, correct_answer = subtract_numbers()
            play_game(num1, num2, correct_answer, "subtract")
        elif choice == "3":
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def play_game(num1, num2, correct_answer, operation):
    guesses = 0

    while True:
        print(f"\n{num1} {operation} {num2}")
        user_answer = int(input("Enter your answer: "))
        guesses += 1

        if user_answer == correct_answer:
            print(f"Congratulations! Your answer is correct.")
            print(f"It took you {guesses} guesses.")
            break
        elif user_answer < correct_answer:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    main()

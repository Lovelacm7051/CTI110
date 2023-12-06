# Simple Math Quiz  

# 12/6/2023

# CTI-110 P5HW - Math Quiz

# Lovelace, Michael

import random

# Initialize variables
num1 = random.randint(1, 999)
num2 = random.randint(1, 999)
correct_answer = num1 + num2
guesses = 0

# Display the math quiz
print(f"Math Quiz: {num1} + {num2}")

# Allow the student to enter the answer
while True:
    user_answer = int(input("Enter your answer: "))
    guesses += 1

    # Check if the answer is correct
    if user_answer == correct_answer:
        print(f"Congratulations! Your answer is correct.")
        print(f"It took you {guesses} guesses.")
        break
    elif user_answer < correct_answer:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

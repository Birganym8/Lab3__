
import random


def guess_the_number():
    number_to_guess = random.randint(1, 20)
    name = input("Hello! What is your name?\n")
    
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    
    guess_count = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        guess = int(input())  
        guess_count += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            guessed_correctly = True
            print(f"Good job, {name}! You guessed my number in {guess_count} guesses!")



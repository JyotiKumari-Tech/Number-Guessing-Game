'''
We are going to write a program that generates a random number and asks the user to guess it. If the player’s guess is higher than the actual number, 
the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher number please” When the user guesses the correct number,
the program displays the number of guesses the player used to arrive at the number.
'''
import random

number = random.randint(1, 100)  # 1 to 100  number range 
guess_count = 0  # for track total guesses

while True:
    try:
        Player_guess_number = int(input("Enter any number to guess: ")) 
        guess_count += 1  # Har guess par counter increment hoga 
        
        if Player_guess_number > number:
            print("Lower number please")
        elif Player_guess_number < number:
            print("Higher number please")
        else:
            print("Correct answer!")
            print(f"You guessed the number in {guess_count} attempts.")  # Total attempts print 
            break  # exit loop when find the correct answer 
    except ValueError:
        print("Invalid input! Please enter a number.")  # Invalid print statement 



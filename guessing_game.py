import random

secret_number = random.randint(0,100)
lst_guess = [0]

rules = """
    We would generate a number for you and you have to guess it correctly. Here are the rules:
    1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
    2. On a player's first turn, if their guess is
        * within 10 of the number, return "WARM!"
        * further than 10 away from the number, return "COLD!"
    3. On all subsequent turns, if a guess is 
        * closer to the number than the previous guess return "WARMER!"
        * farther from the number than the previous guess, return "COLDER!"
    4. When you guess the number correctly, you win!
"""

print(rules)

while True:
    # we can copy the code from above to take an input
    guess = int(input("Guess a number between 0 - 100: ").strip())
    if(guess == secret_number):
        print(f"You guessed the number {secret_number} correctly!!")
        print(f"Number of guesses: {len(lst_guess) - 1}")
        break
    else:
        if(len(lst_guess) == 1):
            if(abs(secret_number - guess) <= 10):
                print("WARM!")
            else:
                print("COLD!")
            
            lst_guess.append(guess)
        else:
            if(abs(secret_number - guess) < abs(secret_number - lst_guess[-1])):
                print("WARMER!")
            else:
                print("COLDER!")
            lst_guess.append(guess)
    pass
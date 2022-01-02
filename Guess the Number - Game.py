import random                                                       # Importing Library for generate random number

highest = 10                                                        # Our highest possible number to guess
answer = random.randint(1, highest)                                 # Our random answer

print("Please guess number between 1 and {}: ".format(highest))     # Our first try to guess number
guess = int(input())
if guess == answer:
    print("You got it first time")                                  # Pop-up in case to guess number first time
else:
    if guess < answer:
        print("Please guess higher")                                # Pop-up in case our guess to low
    else:
        print("Please guess lower")                                 # Pop-up in case our guess to high
    guess = int(input())
    if guess == answer:
        print("Well done, you guess it") # Pop up in case our guess
    else:
        print("Sorry, you have guessed correctly, answer is {} ".format(answer)) # Pop-up in case you didn't guess two times
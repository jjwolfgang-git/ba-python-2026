import random

MIN = 1
MAX = 20
MAX_GUESSES = 7
number = random.randint(MIN, MAX)

num_guesses = 0
guess = MAX+1
correct = False

print(number)

print(f"Pick a number between {MIN} and {MAX}")

while (num_guesses <= MAX_GUESSES and not correct):
    guess = MAX+1
    while (guess < MIN or guess > MAX):
        guess = int(input("> "))

#    print(guess)

    if guess == number:
        correct = True
    elif guess > number:
        print("Too high")
    else:
        print("Too low")

    num_guesses += 1

if correct:
    print("Congrats you got it!")
else:
    print("You lose!")

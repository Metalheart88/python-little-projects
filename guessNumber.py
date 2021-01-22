import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number betweeen 1 and {x}: "))
        if guess > random_number:
            print("Too big. Try a lower number.")
        elif guess < random_number:
            print("Too low. Try something bigger.")
        else:
            print(f"You got it. The correct answer is {random_number}!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if (low != high):
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(
            f'Is {guess} too high (H), too low (L) or correct (C)??').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer guess your number {guess} correctly!')


computer_guess(10)

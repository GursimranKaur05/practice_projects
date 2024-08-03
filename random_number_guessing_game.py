import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!= random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Too low!!")
        elif guess > random_number:
            print("Too high!!")
        
    print(f"Yay!! you have guess the number {random_number} correctly")

guess(5)

def computer_guess(x):
    low = 1
    high = x

    feedback = ''
    while feedback !='c':
        if low != high:
            guess = random.randint(low, high)#randint gives an error if low and high are same
        else:
            guess = low
            
        feedback = input(f"is {guess} too high(H), too low(L) or correct(C)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay!! the computer has guessed your number, {guess}, correctly!')

computer_guess(10)

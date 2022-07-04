import random


def guess(num):
    random_number = random.randint(1, num)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {num}: "))
        if guess < random_number:
            print(f"{guess} is too low")
        elif guess > random_number:
            print(f"{guess} is too high")
    print("Congrats!! You have guessd correctly") 

def comp_guess(num):
    low = 1
    high = num
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = high    
        feedback = input(f"Is {guess} too high(H), too low (L), correct(C): ". lower())
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess +1
    print(f"Congrats!! Computer guessed your number {guess} correctly")        
comp_guess(500)
guess(10)               

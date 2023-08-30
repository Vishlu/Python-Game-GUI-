import random

machine_guess = random.randrange(1,5)

machine_guess_start = 0
while True:
    user_guess = int(input("Enter your number: "))
    print(machine_guess)
    if user_guess == machine_guess: 
        print("Wonderfully played")
        break

    elif user_guess < machine_guess:
        print("Too Law")
        

    elif user_guess > machine_guess:
        print("Too High")
        
    else:
        print("Invalid Type")
        

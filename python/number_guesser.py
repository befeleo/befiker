import random
number_to_guess= random.randint(1,100)
tries=0
while True:
    try:
        guess= int(input("Guess a number between 1-100: "))
        tries+=1
        
        if guess > 100 or guess < 1:
            print("Guess should be between 1-100")
        elif guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations     Number of tries: {tries}")
            again= input("Do you want to continue (y/n? ").lower()
            
            if again=="y":
                number_to_guess= random.randint(1,100)
                tries=0
                continue
            elif again=="n":
                print("Thanks for playing")
                break
        
    except ValueError:
        print("Please enter a valid number")      
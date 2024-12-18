import random

emojis={'r':'🪨', 's':'✂️', 'p':'📃'}
choices= ['r', 's', 'p']

# player_score =0
# computer_score= 0
# player_name= input("Enter your name: ")

while True:
    user_input= input("Rock ,Paper or Scissors? (r, p, s) ").lower()
   

    if user_input not in choices:
        print("Enter a valid input!")
        continue
    computer_input= random.choice(choices)
    if user_input==computer_input:
        print(f"You chose {emojis[user_input]}")
        print(f"Computer chose {emojis[computer_input]}")
        print("Tie")
        # player_score+=1
        # print(f"Score:  {player_name}: player-score Computer: ")
        
    elif ((user_input=='r' and computer_input=='s') or 
    (user_input=='p' and computer_input=='r') or 
    (user_input=='s' and computer_input=='p')):
        print(f"You chose {emojis[user_input]}")
        print(f"Computer chose {emojis[computer_input]}")
        print("You won!") 
        
    else:
        print(f"You chose {emojis[user_input]}")
        print(f"Computer chose {emojis[computer_input]}")
        print("You lose")
        
    should_continue= input("Do you want to continue? (y/n) ")
    if should_continue == 'y':
        
        continue
    else:
        print("Thanks for playing")
        break
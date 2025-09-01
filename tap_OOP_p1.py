## Inputs we need from the user
# total rent
# total food ordered for snacking
# Electricity unit spend
# Charge per unit
# People living in room


## Output
# total amount you have to pay

import random

item_list = ["rock","paper", "scissor"]

computer_choice = random.choice(item_list)
user_choice = input("Enter your choice: ")
print (f"Computer chose {computer_choice}")
if(user_choice == "rock"):
    if(computer_choice == "rock"):
        print("tie")
    elif computer_choice == "scissor":
        print("win")
    else:
        print("lose")
elif user_choice == "paper":
    if(computer_choice == "rock"):
        print("win")
    elif computer_choice == "scissor":
        print("lose")
    else:
        print("tie")
else:
    if(computer_choice == "rock"):
        print("lose")
    elif computer_choice == "scissor":
        print("tie")
    else:
        print("win")
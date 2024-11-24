import random
choices=('r','p','s')
playing=True
while True:
    user_choice=input('Rock,paper or scissors? (r/p/s):').lower()
    if user_choice !='r' and user_choice !='p' and user_choice !='s' :
        print("Please enter a valid choice")
        continue
    computer_choice=random.choice(choices)
    print(f"You choose {user_choice}")
    print(f"Computer choose {computer_choice}")
    if user_choice==computer_choice:
        print("Tie!")
    elif user_choice== 'r' and computer_choice== 's' :
        print("You win !")
    elif user_choice== 's' and computer_choice== 'p':
        print("You win !")
    elif user_choice== 'p' and computer_choice== 'r' :
        print("You win !")
    else:
        print("You lose!")
    should_continue=input("Do you want to continue (y/n):" " ").lower()
    if should_continue== 'n':
        print("Thanks for playing")
        break

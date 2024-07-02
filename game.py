# ROCK, PAPER AND SCISSORS

import random

sys_opt = ["R", "P", "S"]

def sys_game():
    global sys_score
    global user_score
    sys_score = 0
    user_score = 0
    user_ch = ""
    rounds = 0
    while rounds != rounds_to_play:
        user_ch = (input("Enter you choice. Type R for Rock, P for Paper and S for Scissors: ")).upper()
        rounds += 1
        if user_ch in ["R", "P", "S"]:
            print("\nUser choice: ", user_ch)
            sys_ch = random.choice(sys_opt)
            print("System choice: ", sys_ch)
            if user_ch == sys_ch:
                print("Draw")
            elif user_ch == "R" and sys_ch == "P":
                sys_score += 1
                print("User Score: ", user_score, "\nSystem Score: ", sys_score)
            elif user_ch == "R" and sys_ch == "S":
                user_score += 1
                print("User Score: ", user_score, "\nSystem Score: ", sys_score)
            elif user_ch == "P" and sys_ch == "R":
                user_score += 1
                print("User Score: ", user_score, "\nSystem Score: ", sys_score)
            elif user_ch == "P" and sys_ch == "S":
                sys_score += 1
                print("User Score: ", user_score, "\nSystem Score: ", sys_score)
            elif user_ch == "S" and sys_ch == "R":
                sys_score += 1
                print("User Score: ", user_score, "\nSystem Score: ", sys_score)
            elif user_ch == "S" and sys_ch == "P":
                user_score += 1
                print("User Score: ", user_score, "\nSystem Score: ", sys_score)
            elif user_ch not in ["R", "P", "S"]:
                print("Invalid input. Please try again.")
        else:
            return
    print("")
    print("Final Scorecard:\n")
    print(name, " Score: ", user_score)
    print("System Score: ", sys_score)
    if sys_score > user_score:
        print("\nSystem won!!!\n")
    elif sys_score < user_score:
        print("\nCongratulation, ", name, " won!!!\n")
        
def main():
    global name
    global rounds_to_play
    print("=====Welcome to ROCK, PAPER and SCISSORS!!!=====\n")
    name = input("\nEnter your name to play: ")
    print("RULE OF GAME:\n1. Enter R for Rock, S for Scissors and P for Paper as your choice.\n2. You can end the game anytime.")
    rounds_to_play = int(input("Enter the number of rounds you want to play: "))
    sys_game()

if __name__ == "__main__":
    main()
print("Welcome to SNAKE WATER GUN GAME")
print("***********************************************************************")
print("RULES:\n1.SNAKE JUMPS AT WATER SO HE DROP IN WATER SO WATER WON THE GAME",
      "\n2.GUN DROP THE WATER SO WATER WON THE GAME", "\n3.GUN KILL THE SNAKE SO GUN WON THE GAME")
print("***********************************************************************")

computer_score = 0
user_score = 0

i = 1
while (i <= 5):
    # Menu making with computer input start
    s = "SNAKE"
    w = "WATER"
    g = "GUN"

    import random

    computer_num = random.randint(1, 3)
    if (computer_num == 1):
        computer_num = s
    elif (computer_num == 2):
        computer_num = w
    elif (computer_num == 3):
        computer_num = g
    # print(computer_num)
    # Menu making end with compuetr input

    print("\n\n**********");
    print("Round: ", i)
    print("**********")
    print("1.SNAKE\n2.WATER\n3.GUN")
    user_num = int(input('Enter your choice: '))

    # Menu making start with user input
    if (user_num == 1):
        user_num = s
    elif (user_num == 2):
        user_num = w
    elif (user_num == 3):
        user_num = g
    else:
        user_num = "Wrong Input!"
    print(user_num)
    # Menu making end with user input

    # Main Logic Here
    if (computer_num == "SNAKE" and user_num == "WATER"):
        print(f"Computer Choice was {computer_num} and your choice was {user_num} So Computer win the round 1")
        computer_score = computer_score + 1
    elif (computer_num == "WATER" and user_num == "SNAKE"):
        print(f"Computer Choice was {computer_num} and your choice was {user_num} So you win the round 1")
        user_score = user_score + 1
    elif (computer_num == "GUN" and user_num == "WATER"):
        print(f"Computer Choice was {computer_num} and your choice was {user_num} So you win the round 1")
        user_score = user_score + 1
    elif (computer_num == "WATER" and user_num == "GUN"):
        print(f"Computer Choice was {computer_num} and your choice was {user_num} So Computer win the round 1")
        computer_score = computer_score + 1
    elif (computer_num == "GUN" and user_num == "SNAKE"):
        print(f"Computer Choice was {computer_num} and your choice was {user_num} So Computer win the round 1")
        computer_score = computer_score + 1
    elif (computer_num == "SNAKE" and user_num == "GUN"):
        print(f"Computer Choice was {computer_num} and user choice was {user_num} So you win the round 1")
        user_score = user_score + 1
    elif ((computer_num == "SNAKE" and user_num == "SNAKE") or (computer_num == "GUN" and user_num == "GUN") or (
            computer_num == "WATER" and user_num == "WATER")):
        print(f"Computer Choice was {computer_num} and user choice was {user_num} So DRAW THIS ROUND")
        user_score = user_score - 1
        computer_score = computer_score - 1
    else:
        print("Something cause an Unexpected Error By You!")
    i += 1

# Game Over Functionality
print("************************************************")
print("HEY!")
print("GAME OVER!")
print("COMPUTER SCORE: ", computer_score)
print("YOUR SCORE: ", user_score)
if (computer_score > user_score):
    print("Finally Computer is the Winner of the game!")
elif (computer_score < user_score):
    print("Finally User is the Winner of the game!")
elif (computer_score == user_score):
    print("GAME DRAW")

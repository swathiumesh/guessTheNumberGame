import random
from art import logo

EASY = 10
HARD = 5
ANSWER = random.randint(1,100)
print(f"right answer: {ANSWER}")

def play_game():
    print(logo)
    level = input("Select the level: EASY/HARD")
    if level.lower() == "easy":
        level = EASY
    elif level.lower() == "hard":
        level = HARD
    else:
        print("\n" * 20)
        print("Select the right input pleasee")
        play_game()
    guess_the_number(level)

def guess_the_number(level):
    found_ans = "false"
    play_again = "N"
    if level == EASY:
        print("Great, You have 10 chances to guess the number in my mind.. Let's Gooo!!")
    elif level == HARD:
        print("Awesomee, You have 5 chances to guess the number in my mind.. Let's Gooo!!")

    chances = level
    while chances > 0:
        number = int(input("Guess the number between 1-100"))
        if number < ANSWER:
            chances -= 1
            print(f"Too Low, guess again, you have {chances} left :)")
            continue
        elif number > ANSWER:
            chances -= 1
            print(f"Too High, guess again, you have {chances} left :)")
            continue
        elif number == ANSWER:
            chances -= 1
            print(f"Congratulations!!! You guessed the number right, you WIN!!!")
            found_ans = "true"
            break

    if found_ans == "false":
        print("Sorry you lost")
    play_again = input("Want  to try again? Y/N")
    if play_again == "Y":
        play_game()

play_game()



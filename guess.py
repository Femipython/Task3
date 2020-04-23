import random

level = ""
status = True
while status:
    level = input("Choose a level(easy, medium or hard): ")
    if level == "easy":
        secret = random.randint(1, 10)
        guess = 0
        guess_count = 0
        guess_limit = 6
        out_of_guesses = False
        play_again = "Yes"
        chances = 6
        while guess_count < guess_limit and not out_of_guesses:
            try:
                guess_count += 1
                chances -= 1
                guess = int(input(f"Guess a number between 1 - 10, you have {chances} chances left: "))
                if guess == secret:
                    print("You got it right")
                    guess_limit = guess_count
                else:
                    print("That was wrong")
            except ValueError:
                print("Invalid Entry, numbers only")
        if guess_limit == guess_count:
            print("GAME OVER")

    elif level == "medium":
        secret = random.randint(1, 20)
        guess = 0
        guess_count = 0
        guess_limit = 4
        chances = 4
        out_of_guesses = False
        play_again = "Yes"
        while guess_count < guess_limit and not out_of_guesses:
            try:
                chances -= 1
                guess = int(input(f"Guess a number between 1 - 20, you have {chances} chances left: "))
                if guess == secret:
                    print("You got it right")
                    guess_limit = guess_count
                else:
                    print("That was wrong")
                    guess_count += 1
            except ValueError:
                print("Invalid Entry, numbers only")
        if guess_limit == guess_count:
            print("GAME OVER")

    elif level == "hard":
        secret = random.randint(1, 50)
        guess = 0
        guess_count = 0
        guess_limit = 3
        chances = 3
        out_of_guesses = False
        play_again = "Yes"
        while guess_count < guess_limit and not out_of_guesses:
            try:
                chances -= 1
                guess = int(input(f"Guess a number between 1 - 50, you have {chances} chances: "))
                if guess == secret:
                    print("You got it right")
                    guess_limit = guess_count
                else:
                    print("That was wrong")
                    guess_count += 1
            except ValueError:
                print("Invalid Entry, numbers only")
        if guess_limit == guess_count:
            print("GAME OVER")

    else:
        print("Invalid, the available levels are: easy, medium and hard")

    play_again = input("Would you like to play again(Enter Yes or No): ")
    if play_again == "Yes":
        out_of_guesses = False
        status = True
    else:
        status = False


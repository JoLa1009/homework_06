# homework 5.5: Guess the secret number

import random, json, datetime

class Result (object):
    def __init__(self, attempts, player_name, date):
        self.attempts = attempts
        self.player_name = player_name
        self. date = date


def play_game(level):
    attempts = 0
    wrong_guess = []
    secret = random.randint(1, 30)
    lev = level
    if lev == "easy":
        while True:
            guess = int(input("Choose a number between 1 and 30! "))
            attempts += 1
            if guess != secret:
                wrong_guess.append(guess)
                if guess < secret:
                    print("The secret number is bigger. Try it again!")
                else:
                    print("The secret number is smaller. Try it again!")
            else:
                print("Congratulations! You have found the secret number! It is " + str(secret) + "!")
                score_data = {"attempts": attempts, "date": str(datetime.datetime.now()), "name": player,
                          "secret number": str(secret), "wrong guesses": wrong_guess}

                result = Result(attempts,player,str(datetime.datetime.now()))
                score_list = get_score_list()
                score_list.append(result.__dict__)

                from operator import itemgetter
                score_list.sort(key=itemgetter("attempts"))
                score_list.pop(3)

                with open("score_list.txt", "w") as score_file:
                    score_file.write(json.dumps(score_list))

                print("Attempts needed: " + str(attempts))
                print("Wrong guesses: " + str(wrong_guess))
                print()
                break
    else:
        while True:
            guess = int(input("Choose a number between 1 and 30! "))
            attempts += 1
            if guess != secret:
                wrong_guess.append(guess)
                print("Sorry! You haven't found the secret number! Try it again!")
            else:
                print("Congratulations! You have found the secret number! It is " + str(secret) + "!")
                score_data = {"attempts": attempts, "date": str(datetime.datetime.now()), "name": player,
                          "secret number": str(secret), "wrong guesses": wrong_guess}
                score_list = get_score_list()
                score_list.append(score_data)

                from operator import itemgetter
                score_list.sort(key=itemgetter("attempts"))
                score_list.pop(3)

                with open("score_list.txt", "w") as score_file:
                    score_file.write(json.dumps(score_list))

                print("Attempts needed: " + str(attempts))
                print("Wrong guesses: " + str(wrong_guess))
                print()
                break

def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


def top_scores():
    print("Top scores:")
    for score_dict in get_score_list():
        print(
            str(score_dict["name"]) + ": " + str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    print()

player = input("Please enter your name: ")
print()
print("Hello "+player + "!")

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")
    sel = selection.lower()

    if sel == "a":
        selection_level = input("Would you like to play A) the easy level or B) the hard level? ")
        sel_level = selection_level.lower()
        print()
        if sel_level == "a":
            selection = "easy"
        else:
            selection = "hard"
        play_game(selection)

    elif sel == "b":
        print()
        print("Top scores:")
        score_list = get_score_list()
        for score_dict in score_list:
            print(str(score_dict["player_name"]) + ": " + str(score_dict["attempts"]) + " attempts, date: " + score_dict.get(
                "date"))
        print()
    else:
        break

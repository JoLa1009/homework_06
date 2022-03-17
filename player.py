# Homework 6.1
import json

class Player(object):
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

class BasektballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name, last_name, height_cm,weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name, last_name, height_cm,weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

x = input("Do you want to enter some a) football player's or b) basketball player's data? ")
x_low = x.lower()
player_list = []
while True:
    if x_low == "a":
        first_name = input("Enter player's first name: ")
        last_name = input("Enter player's last name: ")
        height = input("Enter player's height: ")
        weight = input("Enter player's weight: ")
        goals = input("Enter the number of goals: ")
        yellow_cards = input("Enter the number of yellow cards: ")
        red_cards = input("Enter the number of red cards: ")
        new_footballer = FootballPlayer(first_name,last_name,height,weight,goals,yellow_cards,red_cards)
        new_footballer_dict = new_footballer.__dict__

        with open("player.txt", "r") as list:
            player_list = json.loads(list.read())

        player_list.append(new_footballer_dict)

        with open ("player.txt","w") as list:
            list.write(json.dumps(player_list))

        print("Player was successfully entered!")
        break

    if x_low == "b":
        first_name = input("Enter player's first name: ")
        last_name = input("Enter player's last name: ")
        height = input("Enter player's height: ")
        weight = input("Enter player's weight: ")
        points = input("Enter the number of points: ")
        rebounds = input("Enter the number of rebounds: ")
        assists = input("Enter the number of assists: ")
        new_basketballer= FootballPlayer(first_name, last_name, height, weight, points, rebounds, assists)
        new_basketballer_dict = new_basketballer.__dict__

        with open("player.txt", "r") as list:
            player_list = json.loads(list.read())

        player_list.append(new_basketballer_dict)

        with open("player.txt", "w") as list:
            list.write(json.dumps(player_list))

        print("Player was successfully entered!")
        break
    else:
        x = input("Please enter an A) or a B) ")
        x_low = x.lower()



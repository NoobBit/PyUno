import random

class Card:
    def __init__(self, type, color):
        self.type = type
        self.color = color

#Create all Cards
repeat_once_type = ["0"]
repeat_twice_types = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "reverse", "skip", "+2"]
repeat_four_types = ["wild", "+4"]
colors = ["red", "yellow", "green", "blue"]

red_cards = []
yellow_cards = []
green_cards = []
blue_cards = []
misc_cards = []

normal_cards = []
total_cards = []

for color in colors:
    if color == "red":
        for ro_card in repeat_once_type:
            red_cards.append(Card(ro_card, "red"))
        for rt_card in repeat_twice_types:
            red_cards.append(Card(rt_card, "red"))
            red_cards.append(Card(rt_card, "red"))

    if color == "yellow":
        for ro_card in repeat_once_type:
            yellow_cards.append(Card(ro_card, "yellow"))
        for rt_card in repeat_twice_types:
            yellow_cards.append(Card(rt_card, "yellow"))
            yellow_cards.append(Card(rt_card, "yellow"))

    if color == "green":
        for ro_card in repeat_once_type:
            green_cards.append(Card(ro_card, "green"))
        for rt_card in repeat_twice_types:
            green_cards.append(Card(rt_card, "green"))
            green_cards.append(Card(rt_card, "green"))

    if color == "blue":
        for ro_card in repeat_once_type:
            blue_cards.append(Card(ro_card, "blue"))
        for rt_card in repeat_twice_types:
            blue_cards.append(Card(rt_card, "blue"))
            blue_cards.append(Card(rt_card, "blue"))

for rf_card in repeat_four_types:
    misc_cards.append(Card(rf_card, "none"))
    misc_cards.append(Card(rf_card, "none"))
    misc_cards.append(Card(rf_card, "none"))
    misc_cards.append(Card(rf_card, "none"))

#Add all Cards
normal_cards.extend(red_cards)
normal_cards.extend(yellow_cards)
normal_cards.extend(green_cards)
normal_cards.extend(blue_cards)
total_cards.extend(normal_cards)
total_cards.extend(misc_cards)

#Give each player their cards
player1_cards = []
player2_cards = []

for card in range(7):
    player1_cards.append(total_cards[random.randint(0, len(total_cards) - 1)])

for card in range(7):
    player2_cards.append(total_cards[random.randint(0, len(total_cards) - 1)])

#Create and filter First Card
first_card = normal_cards[random.randint(0, len(normal_cards) - 1)]

for p1_card in player1_cards:
    print(p1_card.color + ": " + p1_card.type)
print("\n\n")
for p2_card in player1_cards:
    print(p2_card.color + ": " + p2_card.type)
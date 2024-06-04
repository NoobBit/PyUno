import os
import random

class Card:
    def __init__(self, type, color):
        self.type = type
        self.color = color

class Game:
    def __init__(self, player_amount, card_amount):
        self.total_cards, self.normal_cards = self.create_all_cards()
        self.players = self.create_players(player_amount, card_amount)
        self.first_card = self.choose_first_card()
        self.player_amount = player_amount
        self.card_amount = card_amount

    #TEST GAMELOOP SYSTEM
    #TODO: Improve Upon It
    def gameloop(self):
        print(f"Welcome to Uno! There are currently {self.player_amount} players playing with {self.card_amount} cards each!")

        self.last_card_placed = self.first_card
        print(f"The beginning card is a {self.last_card_placed.color} {self.last_card_placed.type}!")

        print(f"\nIt is now player {self.current_player_turn.id}'s turn! Other player(s), please look away from the screen as player {self.current_player_turn.id} chooses their card.")
        input("Press enter to view cards... ")
        os.system('cls' if os.name=='nt' else 'clear')

        self.gameloop_player_choice()


    def create_all_cards(self):
        #TODO: Unhardcode later
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

        return [total_cards, normal_cards]

    def create_players(self, player_amount, cards_per_player):
        list_of_all_players = []
        for player_number in range(player_amount):
            list_of_all_players.append(Player(player_number, self.setup_player_cards(cards_per_player)))

        self.current_player_turn = random.choice(list_of_all_players)
        
        return list_of_all_players

    def setup_player_cards(self, cards_per_player):
        player_cards = []

        for card in range(cards_per_player):
            player_cards.append(self.total_cards[random.randint(0, len(self.total_cards) - 1)])

        return player_cards
    
    def gameloop_player_choice(self):
        print(f"The last card placed is a {self.last_card_placed.color} {self.last_card_placed.type}\n")
        print("You have the following cards...")

        card_increment = 0
        for card in self.current_player_turn.cards:
            card_increment += 1
            if card.color == "none":
                print(f"[{card_increment}] {card.type}")
            else:
                print(f"[{card_increment}] {card.color} {card.type}")
        
        #TODO: Implement Option To Draw Cards If No Cards Match
        player_choice = input("\nPlease choose the number of the card (found on the left) for the card you would like to place: ")

        try:
            int(player_choice)
        except ValueError:
            print("\nUh oh. Please enter the card id number (found on the left) to place that card.")
            input("Please press Enter to continue... ")

            player_choice = ""
            os.system('cls' if os.name=='nt' else 'clear')
            self.gameloop_player_choice()

        try:
            card_chosen = self.current_player_turn.cards[int(player_choice) - 1]
        except IndexError:
            print("\nUh oh. It doesn't seem like this card is in your list. Please enter the card id number (found on the left) to place that card.")
            input("Please press Enter to continue... ")

            player_choice = ""
            os.system('cls' if os.name=='nt' else 'clear')
            self.gameloop_player_choice()
        
        if card_chosen.color != "none":
            print(f"You have chosen the card {card_chosen.color} {card_chosen.type}")
        else:
            print(f"You have chosen the card {card_chosen.type}")
           
    def choose_first_card(self):
        #TODO: Remove +2, reverse, and skip from normal_cards
        first_card = self.normal_cards[random.randint(0, len(self.normal_cards) - 1)]

        #TODO: Remove this trash system which uses a whole different list
        if first_card.type == "reverse" or first_card.type == "+2" or first_card.type == "skip":
            types = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            colors = ["red", "yellow", "green", "blue"]

            first_card = Card(random.choice(types), random.choice(colors))

        return first_card
    
class Player:
    def __init__(self, id, cards):
        self.id = id
        self.cards = cards

game = Game(2, 7)
game.gameloop()

# for player in game.players:
#     print(player.id)
#     for card in player.cards:
#         print(card.color + ": " + card.type)
#     print("\n")
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
        self.queue_direction = 1 #1 means forward; -1 means backward

    #TEST GAMELOOP SYSTEM
    #TODO: Improve Upon It
    def gameloop(self):
        print(f"Welcome to Uno! There are currently {self.player_amount} players playing with {self.card_amount} cards each!")

        self.last_card_placed = self.first_card
        print(f"The beginning card is a {self.last_card_placed.color} {self.last_card_placed.type}!")

        while True:
            print(f"\nIt is now player {self.current_player_turn.id + 1}'s turn! Other player(s), please look away from the screen as player {self.current_player_turn.id + 1} chooses their card.")
            input("Press enter to view cards... ")
            os.system('cls' if os.name=='nt' else 'clear')

            self.gameloop_player_choice()
            if self.queue_direction == 1:
                if self.current_player_turn.id + 1 == len(self.players):
                    self.current_player_turn = self.players[0]
                else:
                    self.current_player_turn = self.players[self.current_player_turn.id + 1]
            elif self.queue_direction == -1:
                if self.current_player_turn.id == 0:
                    self.current_player_turn = self.players[len(self.players) - 1]
                else:
                    self.current_player_turn = self.players[self.current_player_turn.id - 1]

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
            card_chosen = random.choice(self.total_cards)
            player_cards.append(card_chosen)
            self.total_cards.remove(card_chosen)

        return player_cards
    
    def gameloop_player_choice(self):
        player_choice = None
        is_not_acceptable_card = True
        while is_not_acceptable_card:
            if self.last_card_placed.color != "none":
                print(f"The last card placed is a {self.last_card_placed.color} {self.last_card_placed.type}\n")
            else:
                print(f"The last card placed is a {self.last_card_placed.type}\n")
            print("You have the following cards...")

            card_increment = 0
            for card in self.current_player_turn.cards:
                card_increment += 1
                if card.color == "none":
                    print(f"[{card_increment}] {card.type}")
                else:
                    print(f"[{card_increment}] {card.color} {card.type}")
        
            
            print("\nPlease choose the number of the card (found on the left) for the card you would like to place. Or, if you cannot place a card because it doesn't match the last card placed down, please type in \"DRAW\" to draw a new card.")
            player_choice = input()
            if player_choice.lower() == "draw":
                self.gameloop_draw_card(self.current_player_turn)
                break
            elif player_choice.lower() == "exit" or player_choice.lower() == "quit":
                exit(0)

            if not player_choice.isdigit() or int(player_choice) > len(self.current_player_turn.cards) or int(player_choice) < 1:
                print("\nUh oh. It doesn't seem like this card is in your list. Please enter the card id number (found on the left) to place that card.")
                input("Please press Enter to continue... ")
                is_not_acceptable_card = True
                os.system('cls' if os.name=='nt' else 'clear')
            elif self.current_player_turn.cards[int(player_choice) - 1].color != "none":
                if self.current_player_turn.cards[int(player_choice) - 1].type != self.last_card_placed.type and self.current_player_turn.cards[int(player_choice) - 1].color != self.last_card_placed.color:
                    print("\nUh oh. It doesn't seem like this card can be placed. Please choose a card that matches in type, color, or number with the last card placed. If you do not have any cards that meet this requirement, please type in \"DRAW\" to draw a new card.")
                    input("Please press Enter to continue... ")
                    is_not_acceptable_card = True
                    os.system('cls' if os.name=='nt' else 'clear')
                else:
                    is_not_acceptable_card = False
                    break
            else:
                is_not_acceptable_card = False
                break
        if is_not_acceptable_card == False:
            card_chosen = self.current_player_turn.cards[int(player_choice) - 1]
            self.gameloop_play_card(self.current_player_turn, card_chosen)
    
    def gameloop_draw_card(self, player_to_draw_to):
        drawn_card = random.choice(self.total_cards)
        player_to_draw_to.cards.append(drawn_card)
        self.total_cards.remove(drawn_card)

        is_not_acceptable_option = True
        while is_not_acceptable_option:
            if drawn_card.color == "none":
                print(f"\nYou have drawn a {drawn_card.type} card")
            else:
                print(f"\nYou have drawn a {drawn_card.color} {drawn_card.type} card")
        
            print("\nWould you like to...\n[1] Play the card\n[2] Save it and end turn\n[3] Save it and go back to all cards.")
            player_choice = input()

            if not player_choice.isdigit() or (int(player_choice) != 1 and int(player_choice) != 2 and int(player_choice) != 3):
                print("\nUh oh. Invalid Option. Please choose 1, to play the card, 2, to save it and end your turn, or 3, to save it and return to all your cards.")
                input("Please press Enter to continue... ")
                is_not_acceptable_option = True
                os.system('cls' if os.name=='nt' else 'clear')
            elif int(player_choice) == 1:
                if drawn_card.color != "none":
                    if drawn_card.type != self.last_card_placed.type and drawn_card.color != self.last_card_placed.color:
                        print("\nUh oh. It doesn't seem like this card can be placed. Please choose either 2, to save it and end your turn, or 3, to save it and return to all your cards.")
                        input("Please press Enter to continue... ")
                        is_not_acceptable_option = True
                        os.system('cls' if os.name=='nt' else 'clear')
                        continue
                    else:
                        is_not_acceptable_option = False
                        self.gameloop_play_card(player_to_draw_to, drawn_card)
                        break
                else:
                    is_not_acceptable_option = False
                    self.gameloop_play_card(player_to_draw_to, drawn_card)
                    break
            elif int(player_choice) == 2:
                is_not_acceptable_option = False
                os.system('cls' if os.name=='nt' else 'clear')
                print(f"Player {player_to_draw_to.id + 1} drew a card and chose to keep it.\n")
                break
            elif int(player_choice) == 3:
                is_not_acceptable_option = False
                os.system('cls' if os.name=='nt' else 'clear')
                self.gameloop_player_choice()
                break
    
    def gameloop_play_card(self, player, card):
        #TODO: Implement Special Cards
        self.last_card_placed = card
        os.system('cls' if os.name=='nt' else 'clear')

        if card.color != "none":
            print(f"Player {player.id + 1} has played a {card.color} {card.type} card.\n")
        else:
            print(f"Player {player.id + 1} has played a {card.type} card.\n")

        player.cards.remove(card)
           
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
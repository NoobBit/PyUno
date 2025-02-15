import os
import random
import threading
import time
import json

# TODO: Split into Multiple Files
# TODO: Implement Card Stacking (Also With JSON Settings)
# TODO: Enable Colored Text (Also With JSON Settings)
# TODO: Enable/Disable Reverse Card Turning Into Skip Card with Only 2 Players (Also With JSON Settings)

class Card:
    def __init__(self, type, color, modifier):
        self.type = type
        self.color = color
        self.modifier = modifier

class Player:
    def __init__(self, id, cards):
        self.id = id
        self.cards = cards

class Game:
    def __init__(self, player_amount, card_amount, uno_time, settings):
        self.player_amount = player_amount
        self.card_amount = card_amount
        self.uno_time = uno_time
        self.settings = settings

        self.total_cards, self.normal_cards = self.create_all_cards()
        self.players = self.create_players(player_amount, card_amount)
        self.first_card = self.choose_first_card()
        self.queue_direction = 1 #1 means forward; -1 means backward

        self.isGameRunning = True
        self.uno_continue_running = False
        self.uno_successfully_called = False

    #TEST GAMELOOP SYSTEM
    #TODO: Improve Upon It
    def gameloop(self):
        self.clear_screen()

        intro_ascii_art = r"""
 _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _ 
|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|
|_|                                          |_|
|_| ____          __  __                     |_|
|_|/\  _`\       /\ \/\ \                    |_|
|_|\ \ \L\ \__  _\ \ \ \ \    ___     ___    |_|
|_| \ \ ,__/\ \/\ \ \ \ \ \ /' _ `\  / __`\  |_|
|_|  \ \ \/\ \ \_\ \ \ \_\ \/\ \/\ \/\ \L\ \ |_|
|_|   \ \_\ \/`____ \ \_____\ \_\ \_\ \____/ |_|
|_|    \/_/  `/___/> \/_____/\/_/\/_/\/___/  |_|
|_|             /\___/                       |_|
|_|             \/__/                        |_|
|_| _  _  _  _  _  _  _  _  _  _  _  _  _  _ |_|
|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|
"""
        if self.settings.get("show_ascii_art") == True:
            print(intro_ascii_art)
        else:
            print("PyUno")

        print("Created By: NoobBit\n")
        print(f"There are currently {self.player_amount} players playing with {self.card_amount} cards each!")

        self.last_card_placed = self.first_card
        print(f"The beginning card is a {self.last_card_placed.color} {self.last_card_placed.type}!\n")

        while self.isGameRunning:
            print(f"It is now player {self.current_player_turn.id + 1}'s turn! Other player(s), please look away from the screen as player {self.current_player_turn.id + 1} chooses their card.")
            input("Press Enter to view cards... ")
            self.clear_screen()

            self.gameloop_player_choice()

            if self.last_card_placed.type != "skip":
                self.current_player_turn = self.determine_next_player_in_queue(self.current_player_turn)

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
                    red_cards.append(Card(ro_card, "red", "none"))
                for rt_card in repeat_twice_types:
                    red_cards.append(Card(rt_card, "red", "none"))
                    red_cards.append(Card(rt_card, "red", "none"))

            if color == "yellow":
                for ro_card in repeat_once_type:
                    yellow_cards.append(Card(ro_card, "yellow", "none"))
                for rt_card in repeat_twice_types:
                    yellow_cards.append(Card(rt_card, "yellow", "none"))
                    yellow_cards.append(Card(rt_card, "yellow", "none"))

            if color == "green":
                for ro_card in repeat_once_type:
                    green_cards.append(Card(ro_card, "green", "none"))
                for rt_card in repeat_twice_types:
                    green_cards.append(Card(rt_card, "green", "none"))
                    green_cards.append(Card(rt_card, "green", "none"))

            if color == "blue":
                for ro_card in repeat_once_type:
                    blue_cards.append(Card(ro_card, "blue", "none"))
                for rt_card in repeat_twice_types:
                    blue_cards.append(Card(rt_card, "blue", "none"))
                    blue_cards.append(Card(rt_card, "blue", "none"))

        for rf_card in repeat_four_types:
            misc_cards.append(Card(rf_card, "none", "none"))
            misc_cards.append(Card(rf_card, "none", "none"))
            misc_cards.append(Card(rf_card, "none", "none"))
            misc_cards.append(Card(rf_card, "none", "none"))

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
    
    def clear_screen(self):
        os.system('cls' if os.name=='nt' else 'clear')
    
    def gameloop_print_last_placed_card(self):
        if self.last_card_placed.color != "none":
            print(f"The last card placed is a {self.last_card_placed.color} {self.last_card_placed.type}\n")
        else:
            print(f"The last card placed is a {self.last_card_placed.type} card with the color {self.last_card_placed.modifier}\n")
    
    def gameloop_player_choice(self):
        player_choice = None
        is_not_acceptable_card = True
        while is_not_acceptable_card:
            self.gameloop_print_last_placed_card()
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

            elif player_choice.lower() == "exit" and self.settings.get("allow_debug_commands"):
                exit(0)

            if not player_choice.isdigit() or int(player_choice) > len(self.current_player_turn.cards) or int(player_choice) < 1:
                print("\nUh oh. It doesn't seem like this card is in your list. Please enter the card id number (found on the left) to place that card.")
                input("Please press Enter to continue... ")
                is_not_acceptable_card = True
                self.clear_screen()
            elif self.current_player_turn.cards[int(player_choice) - 1].color != "none":
                if self.current_player_turn.cards[int(player_choice) - 1].type != self.last_card_placed.type and self.current_player_turn.cards[int(player_choice) - 1].color != self.last_card_placed.color and self.current_player_turn.cards[int(player_choice) - 1].color != self.last_card_placed.modifier:
                    print("\nUh oh. It doesn't seem like this card can be placed. Please choose a card that matches in type, color, or number with the last card placed. If you do not have any cards that meet this requirement, please type in \"DRAW\" to draw a new card.")
                    input("Please press Enter to continue... ")
                    is_not_acceptable_card = True
                    self.clear_screen()
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
            self.clear_screen()
            if drawn_card.color == "none":
                print(f"You have drawn a {drawn_card.type} card\n")
            else:
                print(f"You have drawn a {drawn_card.color} {drawn_card.type} card\n")
            
            self.gameloop_print_last_placed_card()
        
            print("Would you like to...\n[1] Play the card\n[2] Save it and end turn\n[3] Save it and go back to all cards.")
            player_choice = input()

            if not player_choice.isdigit() or (int(player_choice) != 1 and int(player_choice) != 2 and int(player_choice) != 3):
                print("\nUh oh. Invalid Option. Please choose 1, to play the card, 2, to save it and end your turn, or 3, to save it and return to all your cards.")
                input("Please press Enter to continue... ")
                is_not_acceptable_option = True
            elif int(player_choice) == 1:
                if drawn_card.color != "none":
                    if drawn_card.type != self.last_card_placed.type and drawn_card.color != self.last_card_placed.color and drawn_card.color != self.last_card_placed.modifier:
                        print("\nUh oh. It doesn't seem like this card can be placed. Please choose either 2, to save it and end your turn, or 3, to save it and return to all your cards.")
                        input("Please press Enter to continue... ")
                        is_not_acceptable_option = True
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
                self.clear_screen()
                print(f"Player {player_to_draw_to.id + 1} drew a card and chose to keep it.\n")
                break
            elif int(player_choice) == 3:
                is_not_acceptable_option = False
                self.clear_screen()
                self.gameloop_player_choice()
                break
    
    def gameloop_play_card(self, player, card):
        #TODO: Implement Special Cards

        #Wild and +4 Cards
        if card.type == "wild" or card.type == "+4":
            is_not_acceptable_option = True
            while is_not_acceptable_option:
                self.clear_screen()
                print(f"You have chosen to place down a {card.type} card.\n")
                self.gameloop_print_last_placed_card()
                print("Here are the following colors you can switch to...\n[1] Red\n[2] Yellow\n[3] Green\n[4] Blue")
                player_choice = input()
                if not player_choice.isdigit() or (int(player_choice) != 1 and int(player_choice) != 2 and int(player_choice) != 3 and int(player_choice) != 4):
                    print("\nUh oh. Invalid Option. Please choose 1 for red, 2 for yellow, 3 for green, or 4 for blue.")
                    input("Please press Enter to continue... ")
                    is_not_acceptable_option = True
                elif int(player_choice) == 1:
                    if card.type == "+4":
                        self.gameloop_play_four_plus_card(card, "red", player)
                    else:
                        self.gameloop_play_wild_card(card, "red", player) 
                    is_not_acceptable_option = False
                elif int(player_choice) == 2:
                    if card.type == "+4":
                        self.gameloop_play_four_plus_card(card, "yellow", player)
                    else:
                        self.gameloop_play_wild_card(card, "yellow", player) 
                    is_not_acceptable_option = False
                elif int(player_choice) == 3:
                    if card.type == "+4":
                        self.gameloop_play_four_plus_card(card, "green", player)
                    else:
                        self.gameloop_play_wild_card(card, "green", player) 
                    is_not_acceptable_option = False
                elif int(player_choice) == 4:
                    if card.type == "+4":
                        self.gameloop_play_four_plus_card(card, "blue", player)
                    else:
                        self.gameloop_play_wild_card(card, "blue", player) 
                    is_not_acceptable_option = False
        #2+ Card
        elif card.type == "+2":
            self.gameloop_play_two_plus_card(card, player)
        #Reverse
        elif card.type == "reverse":
            self.last_card_placed = card

            self.queue_direction *= -1 #Changes 1 -> -1 and -1 -> 1
            next_player = self.determine_next_player_in_queue(self.current_player_turn)

            player.cards.remove(card)
            self.gameloop_check_card_numbers(player)

            print(f"Player {player.id + 1} has placed a {card.color} {card.type} card and has changed the direction of the game to player {next_player.id + 1}\n")
        #Skip
        elif card.type == "skip":
            self.last_card_placed = card

            skipped_over_player = self.determine_next_player_in_queue(self.current_player_turn)
            real_next_player = self.determine_next_player_in_queue(skipped_over_player)
            self.current_player_turn = real_next_player

            player.cards.remove(card)
            self.gameloop_check_card_numbers(player)

            print(f"Player {player.id + 1} has placed a {card.color} {card.type} card and skipped player {skipped_over_player.id + 1}'s turn.\n")               
        #Normal Cards
        else:
            self.last_card_placed = card

            player.cards.remove(card)
            self.gameloop_check_card_numbers(player)

            if card.color != "none":
                print(f"Player {player.id + 1} has played a {card.color} {card.type} card.\n")
            else:
                print(f"Player {player.id + 1} has played a {card.type} card.\n")
    
    def gameloop_play_wild_card(self, card, color, player):
        card.modifier = color
        self.last_card_placed = card

        player.cards.remove(card)
        self.gameloop_check_card_numbers(player)

        print(f"Player {player.id + 1} has placed a {card.type} card with the color {card.modifier}\n")
    
    def gameloop_play_four_plus_card(self, card, color, player):
        card.modifier = color
        self.last_card_placed = card
        next_player = self.determine_next_player_in_queue(self.current_player_turn)

        self.gameloop_draw_x_cards(4, next_player)
        player.cards.remove(card)
        self.gameloop_check_card_numbers(player)

        print(f"Player {player.id + 1} has placed a {card.type} card on player {next_player.id + 1} with the color {card.modifier}\n")

    def gameloop_play_two_plus_card(self, card, player):
        self.last_card_placed = card
        next_player = self.determine_next_player_in_queue(self.current_player_turn)
        
        self.gameloop_draw_x_cards(2, next_player)
        player.cards.remove(card)
        self.gameloop_check_card_numbers(player)

        print(f"Player {player.id + 1} has placed a {card.color} {card.type} card on player {next_player.id + 1}\n")
                        
    def gameloop_draw_x_cards(self, card_number, player_to_draw_to):
        for i in range(card_number):
            drawn_card = random.choice(self.total_cards)
            player_to_draw_to.cards.append(drawn_card)
            self.total_cards.remove(drawn_card)
    
    def gameloop_activate_uno_message(self, time_left, player):
        while self.uno_continue_running:
            if not time_left <= 0:
                self.clear_screen()
                
                ascii_message = f"""╔═════════════════════════════╗
║ PRESS ENTER TO DECLARE UNO! ║
║                             ║
║ YOU HAVE {time_left}s REMAINING !!!! ║
╚═════════════════════════════╝
"""
                normal_message = f"PRESS ENTER TO DECLARE UNO! YOU HAVE {time_left}s REMAINING !!!!"

                if self.settings.get("show_ascii_art") == True:
                    print(ascii_message)
                else:
                    print(normal_message)

                time.sleep(1)
                time_left -= 1
            else:
                self.uno_continue_running = False
                self.gameloop_draw_x_cards(2, player)

                self.clear_screen()
                print("You have failed to declare an UNO, and therefore, you now have recieved two new cards. Next time, make sure to press \"Enter\" before the time runs out. Press Enter to end your turn.")
                self.uno_successfully_called = False

    def gameloop_check_card_numbers(self, player):
        if len(player.cards) == 1:
            self.uno_continue_running = True
            self.uno_successfully_called = True

            uno_thread = threading.Thread(target=self.gameloop_activate_uno_message, args=(self.uno_time, player,))
            uno_thread.start()
            uno_thread = input()

            if uno_thread != None:
                self.uno_continue_running = False
            
            if self.uno_successfully_called:
                self.uno_successfully_called = False
                self.clear_screen()
                print("Congratulations! You successfully declared an UNO. You now have one card remaining... Press Enter to end your turn.")
                input()

                self.clear_screen()
                print(f"Player {player.id + 1} has successfully declared an UNO. They now have one card remaining...")
            else:
                self.clear_screen()
                print(f"Player {player.id + 1} has failed to declare an UNO. As a resulty, they recieved two additional cards.")
        elif len(player.cards) == 0:
            self.clear_screen()
            self.end_game(player)
        else:
            self.clear_screen()
            print(f"Player {player.id + 1} now has {len(player.cards)} cards remaining...")

    def choose_first_card(self):
        #TODO: Remove +2, reverse, and skip from normal_cards
        first_card = self.normal_cards[random.randint(0, len(self.normal_cards) - 1)]

        #TODO: Remove this trash system which uses a whole different list
        if first_card.type == "reverse" or first_card.type == "+2" or first_card.type == "skip":
            types = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            colors = ["red", "yellow", "green", "blue"]

            first_card = Card(random.choice(types), random.choice(colors), "none")

        return first_card

    def determine_next_player_in_queue(self, current_player):
        if self.queue_direction == 1:
            if current_player.id + 1 == len(self.players):
                return self.players[0]
            else:
                return self.players[current_player.id + 1]
        elif self.queue_direction == -1:
            if current_player.id == 0:
                return self.players[len(self.players) - 1]
            else:
                return self.players[current_player.id - 1]
            
    def end_game(self, victor):
        self.isGameRunning = False

        victory_ascii_art = r"""
 _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _ 
|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|
|_|                                                         |_|
|_| __  __              __                          __      |_|
|_|/\ \/\ \  __        /\ \__                      /\ \     |_|
|_|\ \ \ \ \/\_\    ___\ \ ,_\   ___   _ __   __  _\ \ \    |_|
|_| \ \ \ \ \/\ \  /'___\ \ \/  / __`\/\`'__\/\ \/\ \ \ \   |_|
|_|  \ \ \_/ \ \ \/\ \__/\ \ \_/\ \L\ \ \ \/ \ \ \_\ \ \_\  |_|
|_|   \ `\___/\ \_\ \____\\ \__\ \____/\ \_\  \/`____ \/\_\ |_|
|_|    `\/__/  \/_/\/____/ \/__/\/___/  \/_/   `/___/> \/_/ |_|
|_|                                               /\___/    |_|
|_|                                               \/__/     |_|
|_| _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _ |_|
|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|
"""
        if self.settings.get("show_ascii_art") == True:
            print(victory_ascii_art)
        else:
            print("Victory!")
        print(f"Congratulations, Player {victor.id + 1}! You have won the game by successfully playing all your cards!\n")
        
        list_of_losers = self.players.copy()
        list_of_losers.remove(victor)

        if len(list_of_losers) != 1:
            print("The following list contains how close the other players were to winning...\n")
            for loser in list_of_losers:
                print(f"Player {loser.id + 1}: {len(loser.cards)} card(s) remaining.")
        else:
            print(f"Player {list_of_losers[0].id + 1} was close to victory having {len(list_of_losers[0].cards)} card(s) in the end!")
        print()
        exit(0)

# TODO: Add More Settings
def extract_json_settings(settings_filename):
    with open(settings_filename, "r") as file:
        settings_content = json.load(file)
        return settings_content

def fix_missing_json_settings(settings_content):
    if settings_content.get("player_amount") == None: settings_content.update({"player_amount": 2})
    if settings_content.get("card_amount") == None: settings_content.update({"card_amount": 7})
    if settings_content.get("uno_time") == None: settings_content.update({"uno_time": 3})
    if settings_content.get("show_ascii_art") == None: settings_content.update({"show_ascii_art": True})
    if settings_content.get("allow_debug_commands") == None: settings_content.update({"allow_debug_commands": False})

    return settings_content

if __name__ == "__main__":
    settings_content = extract_json_settings("game_settings.json")
    settings_content = fix_missing_json_settings(settings_content)

    game = Game(settings_content.get("player_amount"), settings_content.get("card_amount"), settings_content.get("uno_time"), settings_content)
    game.gameloop()
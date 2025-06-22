# PyUno 🔴🟡🟢🔵
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#) [![Card](https://img.shields.io/badge/game-UNO-red)](#) 
### A fun game adaptation of the popular card game UNO in Python.
PyUNO is a simple terminal game based off the card game UNO. Built with Python, it features rich ASCII art, multiple player functionality, and so much more!

![pyuno-screenshot-1](https://github.com/user-attachments/assets/c8e571f1-e5ce-48cd-ba2a-97a5d4c79749)

## Table Of Contents
1. [Features](#features)
2. [Screenshots](#screenshots)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Final Note](#final-note)

## Features
- ASCII Art
- Multiple-Player Functionality
- Core UNO Game
- Custom Settings (Through JSON)
- So Much More!

## Screenshots
### Card Interface
![pyuno-screenshot-2](https://github.com/user-attachments/assets/2fc4d3b7-c1dc-476b-a9e2-819a7b347107)
### Multiple-Player Functionality
![pyuno-screenshot-3](https://github.com/user-attachments/assets/2564ff8f-a06e-4fb5-827e-1fd46222fa06)
### Uno Declaration
![pyuno-screenshot-7](https://github.com/user-attachments/assets/167a5785-efe6-4b3b-8510-2ecb0e2c5ae1)
### Victory Screen
![pyuno-screenshot-4](https://github.com/user-attachments/assets/45ab8cb5-8b36-413f-b716-e506464a5663)

## Installation
### Prerequsites:
In order to play PyUNO and ensure all features properly work, please ensure you have Python installed (preferably 3.13 or higher). Install Python Here: [Download Python](https://www.python.org/downloads/)
### Step #1: Obtain Source Code
#### Method #1: Git
Open your terminal of preference and enter the following command. Please ensure you have git installed.
```
git clone https://github.com/NoobBit/PyUno.git
cd PyUno
python main.py
```
#### Method #2: Github Download
On this page, click the "<> Code" button and click "Download ZIP". Alternatively, click this link: [Download Here](https://github.com/NoobBit/PyUno/archive/refs/heads/main.zip)
Then extract the files and open your terminal of preference in the folder. Then run:
```
python main.py
```

## Usage
Before playing PyUno, please make sure you understand how to play Uno. [Rule Book](https://www.unorules.com/)
### Introduction
Upon running the game, you will be met by the introduction screen, containing the PyUno Logo. This screen provides information about the number of players, the number of cards per player, the player whose turn is first, and the beginning card.

![pyuno-screenshot-1](https://github.com/user-attachments/assets/c8e571f1-e5ce-48cd-ba2a-97a5d4c79749)

### Card Interface
During a player's turn, they will be prompted with the card interface screen. This screen displays all their cards, the last played card, and their possible actions. 
The user has two main possible actions: place a card by selecting the card number (1, 2, 3, etc.) OR DRAW, which draws a card from the deck.

![pyuno-screenshot-2](https://github.com/user-attachments/assets/2fc4d3b7-c1dc-476b-a9e2-819a7b347107)

### Draw Interface
When the player draws a card during their turn, they will be met by the draw interface screen. This screen shows the possible actions a player can take: play the card, save the card and end their turn, or save their card and go back to the card interface.

![pyuno-screenshot-5](https://github.com/user-attachments/assets/918b3ea8-13af-4c98-9ce8-776e4db75e95)

### Color Selection
If a player places down a Wild Card or +4 Card, they will be prompted with the color selection screen. On the screen, the player must choose the color they would like to switch to by entering in 1, 2, 3, or 4, corresponding to red, yellow, green, and blue respectively.

![pyuno-screenshot-6](https://github.com/user-attachments/assets/f6f4d4b6-fe16-4f6f-ab8e-288263e0e378)

### End of Turn
Once a player places a card (or doesn't by ending their turn), both players will be met by the end of turn screen. On this screen, the player who was just playing should transfer the screen to the other player. The initial player should not look at the other player's screen until the end of their turn.

![pyuno-screenshot-3](https://github.com/user-attachments/assets/2564ff8f-a06e-4fb5-827e-1fd46222fa06)

### UNO Declaration
Nearing the end game, when a player has one card remaining, they will quickly receive the uno declaration screen. During the time frame, the user must press the "Enter" key to declare an UNO. If the user fails to declare an UNO, they will receive two extra cards. Successful declaration will result in no punishment.

![pyuno-screenshot-7](https://github.com/user-attachments/assets/167a5785-efe6-4b3b-8510-2ecb0e2c5ae1)

### Victory
Once a player has successfully won the game by disposing of all of their cards, all players will be met by the victory screen. This final screen displays important final information like the player who won and how close the other player(s) were to winning.

![pyuno-screenshot-4](https://github.com/user-attachments/assets/45ab8cb5-8b36-413f-b716-e506464a5663)

### Settings
PyUno can be customized using the provided `game_settings.json` file. By editing values in the file, you can customize:
- The number of players
- The number of cards per player
- The amount of time to declare UNO
- The ability to see the ASCII art
- The ability to toggle debug commands
- And more (coming in the future)

![pyuno-screenshot-8](https://github.com/user-attachments/assets/457fd7b8-7af8-4677-a2b0-b0aa8aa6c94e)

Deleting and/or not including this file within the same directory as PyUno may result in unexpected behavior. 

## Final Note
PyUno is still in development with many new features coming. If you would like to support this project, please feel free to star it and contribute to the code. I would greatly appreciate it!

Enjoy! 😀

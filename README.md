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

### Wild Card

### End of Turn
Once a player places a card (or doesn't by ending their turn), both players will be met by the end of turn screen. On this screen, the player who was just playing should transfer the screen to the other player. The initial player should not look at the other player's screen until the end of their turn.

![pyuno-screenshot-3](https://github.com/user-attachments/assets/2564ff8f-a06e-4fb5-827e-1fd46222fa06)

### UNO

### Victory
Once a player has successfully won the game by disposing of all of their cards, all players will be met by the victory screen. This final screen displays important final information like the player who won and how close the other player(s) were to winning.

![pyuno-screenshot-4](https://github.com/user-attachments/assets/45ab8cb5-8b36-413f-b716-e506464a5663)

### Settings

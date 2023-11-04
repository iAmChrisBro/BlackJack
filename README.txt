Group #2 (Jian Mejia, Christan Perez, Sean Perez)
-----------------------Creator Roles--------------------
Jian Mejia - program main game screen and game mechanics
Christian Perez - program stats screen and menu screen
Sean Perez - demo video

-----------------------Designers----------------------------
Christian Perez
Jian Mejia

-----------------------DeBuggers----------------------------
Jian Mejia
Christian Perez

-----------------------Citation----------------------------------
card images- https://code.google.com/archive/p/vector-playing-cards/

-------------------Requirements-----------------------------
- Pillow library
- Python 3

-----------How to Install Python----------------------------
1. go to https://www.python.org/downloads/
2. click download python
3. open python installer
4. go through installation process

-----------How to Install Pillow Library--------------------
(Windows)
1. have python installed
2. open command prompt
3. type "pip install Pillow" in the command prompt (case sensitive)
4. pillow is installed

------------How to Start Game-----------------------------
1. install libraries and python 3
2. open main.py

--------------Blackjack Rules(classic, no split, no double down)-----------------
(Objective)
Get your total card value as close to 21 as possible while trying to get a better total card value than the dealer without going over by drawing playing cards.

(Card Values)
Ace = 1 or 11
2 = 2
3 = 3
4 = 4
5 = 5
6 = 6
7 = 7
8 = 8
9 = 9
Jack = 10
Queen = 10
King = 10

(Terms)
Hit - draw a card
Stand - keep cards and end turn
Blackjack - card total equals 21
Push - card total is equal to that of the dealer
Player Wins - card total is greater than that of the dealer
Dealer Wins - card total is less than that of the dealer

(results)
Blackjack - add amount bet to balance with 50% bonus
Push - keep money
Player Wins - add amount bet to balance
Dealer Wins - subtract amount bet from balance
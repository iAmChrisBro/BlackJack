import tkinter
from PIL import Image, ImageTk
import random
from tkinter import ttk
main = tkinter.Tk()
#screen parameters
xGeo = 300
yGeo = 300
main.geometry(str(xGeo) + "x" + str(yGeo))
main.resizable(width = False, height = False)
main.title("Blackjack")
#--frames--
scrnBlackjack = tkinter.Frame(main)
scrnBlackjack.place(x=0, y=0, relwidth=1.0, relheight=1.0)
scrnStats = tkinter.Frame(main)
scrnStats.place(x=0, y=0, relwidth=1.0, relheight=1.0)
scrnTitle = tkinter.Frame(main)
scrnTitle.place(x=0, y=0, relwidth=1.0, relheight=1.0)
#---------------------------------------
#--user data--
#the amount balance that is typed in the text box
tempBalance = tkinter.IntVar()
#the amount of money the player has
balance = 0
#the amount that is bet that is typed in the text box
tempBet = tkinter.IntVar()
#the amount of money the player is betting
bet = 0
#y axis the players cards are going to be on
playerCardYPos = round(yGeo * (7/10))
#the cards that the player has
playerCards = []
#the total that the pl ayer has
playerTotal = 0
playerTotalAlt = 0
playerTotalBase = 0
playerBestHand = 0
#the total number of games won
roundsWon = 0
#the total number of games lost
roundsLost = 0
#number of games played
roundsPlayed = roundsWon + roundsLost
#--------------------------------------------
#--computer data--
#y axis the computers cards are going to be on
computerCardYPos = round (yGeo * (2/10))
#cards that the computer has
computerCards = []
#total that the computer has
computerTotal = 0
computerTotalAlt = 0
computerTotalBase = 0
computerHiddenValue = 0
tempCompTotal = 0
computerBestHand = 0
#-----------------------------------------------------
#--card data--
#initial card position
initialX = 10000
initialY = 10000
cardHeight = yGeo / 6
#gets card width... dont change
cardWidth = (500 / 726) * cardHeight
cardArray = []
#card images
#heart card paths
pathImgCardH1 = Image.open("images/ace_of_hearts.png")
pathImgCardH2 = Image.open("images/2_of_hearts.png")
pathImgCardH3 = Image.open("images/3_of_hearts.png")
pathImgCardH4 = Image.open("images/4_of_hearts.png")
pathImgCardH5 = Image.open("images/5_of_hearts.png")
pathImgCardH6 = Image.open("images/6_of_hearts.png")
pathImgCardH7 = Image.open("images/7_of_hearts.png")
pathImgCardH8 = Image.open("images/8_of_hearts.png")
pathImgCardH9 = Image.open("images/9_of_hearts.png")
pathImgCardH10 = Image.open("images/10_of_hearts.png")
pathImgCardH11 = Image.open("images/jack_of_hearts.png")
pathImgCardH12 = Image.open("images/queen_of_hearts.png")
pathImgCardH13 = Image.open("images/king_of_hearts.png")
#spade card variables
pathImgCardS1 = Image.open("images/ace_of_spades.png")
pathImgCardS2 = Image.open("images/2_of_spades.png")
pathImgCardS3 = Image.open("images/3_of_spades.png")
pathImgCardS4 = Image.open("images/4_of_spades.png")
pathImgCardS5 = Image.open("images/5_of_spades.png")
pathImgCardS6 = Image.open("images/6_of_spades.png")
pathImgCardS7 = Image.open("images/7_of_spades.png")
pathImgCardS8 = Image.open("images/8_of_spades.png")
pathImgCardS9 = Image.open("images/9_of_spades.png")
pathImgCardS10 = Image.open("images/10_of_spades.png")
pathImgCardS11 = Image.open("images/jack_of_spades.png")
pathImgCardS12 = Image.open("images/queen_of_spades.png")
pathImgCardS13 = Image.open("images/queen_of_spades.png")
#club card paths
pathImgCardC1 = Image.open("images/ace_of_clubs.png")
pathImgCardC2 = Image.open("images/2_of_clubs.png")
pathImgCardC3 = Image.open("images/3_of_clubs.png")
pathImgCardC4 = Image.open("images/4_of_clubs.png")
pathImgCardC5 = Image.open("images/5_of_clubs.png")
pathImgCardC6 = Image.open("images/6_of_clubs.png")
pathImgCardC7 = Image.open("images/7_of_clubs.png")
pathImgCardC8 = Image.open("images/8_of_clubs.png")
pathImgCardC9 = Image.open("images/9_of_clubs.png")
pathImgCardC10 = Image.open("images/10_of_clubs.png")
pathImgCardC11 = Image.open("images/jack_of_clubs.png")
pathImgCardC12 = Image.open("images/queen_of_clubs.png")
pathImgCardC13 = Image.open("images/king_of_clubs.png")
#diamond card paths
pathImgCardD1 = Image.open("images/ace_of_diamonds.png")
pathImgCardD2 = Image.open("images/2_of_diamonds.png")
pathImgCardD3 = Image.open("images/3_of_diamonds.png")
pathImgCardD4 = Image.open("images/4_of_diamonds.png")
pathImgCardD5 = Image.open("images/5_of_diamonds.png")
pathImgCardD6 = Image.open("images/6_of_diamonds.png")
pathImgCardD7 = Image.open("images/7_of_diamonds.png")
pathImgCardD8 = Image.open("images/8_of_diamonds.png")
pathImgCardD9 = Image.open("images/9_of_diamonds.png")
pathImgCardD10 = Image.open("images/10_of_diamonds.png")
pathImgCardD11 = Image.open("images/jack_of_diamonds.png")
pathImgCardD12 = Image.open("images/queen_of_diamonds.png")
pathImgCardD13 = Image.open("images/king_of_diamonds.png")
#back card path
pathImgCardBack = Image.open("images/card_back.png")
imgPathList = [ pathImgCardH1, pathImgCardH2, pathImgCardH3, pathImgCardH4, pathImgCardH5, pathImgCardH6, pathImgCardH7, pathImgCardH8, pathImgCardH9, pathImgCardH10, pathImgCardH11, pathImgCardH12, pathImgCardH13, pathImgCardS1, pathImgCardS2, pathImgCardS3, pathImgCardS4, pathImgCardS5, pathImgCardS6, pathImgCardS7, pathImgCardS8, pathImgCardS9, pathImgCardS10, pathImgCardS11, pathImgCardS12, pathImgCardS13, pathImgCardC1, pathImgCardC2, pathImgCardC3, pathImgCardC4, pathImgCardC5, pathImgCardC6, pathImgCardC7, pathImgCardC8, pathImgCardC9, pathImgCardC10, pathImgCardC11, pathImgCardC12, pathImgCardC13, pathImgCardD1, pathImgCardD2, pathImgCardD3, pathImgCardD4, pathImgCardD5, pathImgCardD6, pathImgCardD7, pathImgCardD8, pathImgCardD9, pathImgCardD10, pathImgCardD11, pathImgCardD12, pathImgCardD13, pathImgCardBack]
for x in imgPathList:
	x = x.thumbnail((round(cardWidth), round(cardHeight)), Image.ANTIALIAS)
#heart card photoimages
photoImgCardH1 = ImageTk.PhotoImage(pathImgCardH1)
photoImgCardH2 = ImageTk.PhotoImage(pathImgCardH2)
photoImgCardH3 = ImageTk.PhotoImage(pathImgCardH3)
photoImgCardH4 = ImageTk.PhotoImage(pathImgCardH4)
photoImgCardH5 = ImageTk.PhotoImage(pathImgCardH5)
photoImgCardH6 = ImageTk.PhotoImage(pathImgCardH6)
photoImgCardH7 = ImageTk.PhotoImage(pathImgCardH7)
photoImgCardH8 = ImageTk.PhotoImage(pathImgCardH8)
photoImgCardH9 = ImageTk.PhotoImage(pathImgCardH9)
photoImgCardH10 = ImageTk.PhotoImage(pathImgCardH10)
photoImgCardH11 = ImageTk.PhotoImage(pathImgCardH11)
photoImgCardH12 = ImageTk.PhotoImage(pathImgCardH12)
photoImgCardH13 = ImageTk.PhotoImage(pathImgCardH13)
#spade card photoimages
photoImgCardS1 = ImageTk.PhotoImage(pathImgCardS1)
photoImgCardS2 = ImageTk.PhotoImage(pathImgCardS2)
photoImgCardS3 = ImageTk.PhotoImage(pathImgCardS3)
photoImgCardS4 = ImageTk.PhotoImage(pathImgCardS4)
photoImgCardS5 = ImageTk.PhotoImage(pathImgCardS5)
photoImgCardS6 = ImageTk.PhotoImage(pathImgCardS6)
photoImgCardS7 = ImageTk.PhotoImage(pathImgCardS7)
photoImgCardS8 = ImageTk.PhotoImage(pathImgCardS8)
photoImgCardS9 = ImageTk.PhotoImage(pathImgCardS9)
photoImgCardS10 = ImageTk.PhotoImage(pathImgCardS10)
photoImgCardS11 = ImageTk.PhotoImage(pathImgCardS11)
photoImgCardS12 = ImageTk.PhotoImage(pathImgCardS12)
photoImgCardS13 = ImageTk.PhotoImage(pathImgCardS13)
#club card photoimages
photoImgCardC1 = ImageTk.PhotoImage(pathImgCardC1)
photoImgCardC2 = ImageTk.PhotoImage(pathImgCardC2)
photoImgCardC3 = ImageTk.PhotoImage(pathImgCardC3)
photoImgCardC4 = ImageTk.PhotoImage(pathImgCardC4)
photoImgCardC5 = ImageTk.PhotoImage(pathImgCardC5)
photoImgCardC6 = ImageTk.PhotoImage(pathImgCardC6)
photoImgCardC7 = ImageTk.PhotoImage(pathImgCardC7)
photoImgCardC8 = ImageTk.PhotoImage(pathImgCardC8)
photoImgCardC9 = ImageTk.PhotoImage(pathImgCardC9)
photoImgCardC10 = ImageTk.PhotoImage(pathImgCardC10)
photoImgCardC11 = ImageTk.PhotoImage(pathImgCardC11)
photoImgCardC12 = ImageTk.PhotoImage(pathImgCardC12)
photoImgCardC13 = ImageTk.PhotoImage(pathImgCardC13)
#diamond card photoimages
photoImgCardD1 = ImageTk.PhotoImage(pathImgCardD1)
photoImgCardD2 = ImageTk.PhotoImage(pathImgCardD2)
photoImgCardD3 = ImageTk.PhotoImage(pathImgCardD3)
photoImgCardD4 = ImageTk.PhotoImage(pathImgCardD4)
photoImgCardD5 = ImageTk.PhotoImage(pathImgCardD5)
photoImgCardD6 = ImageTk.PhotoImage(pathImgCardD6)
photoImgCardD7 = ImageTk.PhotoImage(pathImgCardD7)
photoImgCardD8 = ImageTk.PhotoImage(pathImgCardD8)
photoImgCardD9 = ImageTk.PhotoImage(pathImgCardD9)
photoImgCardD10 = ImageTk.PhotoImage(pathImgCardD10)
photoImgCardD11 = ImageTk.PhotoImage(pathImgCardD11)
photoImgCardD12 = ImageTk.PhotoImage(pathImgCardD12)
photoImgCardD13 = ImageTk.PhotoImage(pathImgCardD13)
#photoimages array
photoImageArray = [ photoImgCardH1, photoImgCardH2, photoImgCardH3, photoImgCardH4, photoImgCardH5, photoImgCardH6, photoImgCardH7, photoImgCardH8, photoImgCardH9, photoImgCardH10, photoImgCardH11, photoImgCardH12, photoImgCardH13, photoImgCardS1, photoImgCardS2, photoImgCardS3, photoImgCardS4, photoImgCardS5, photoImgCardS6, photoImgCardS7, photoImgCardS8, photoImgCardS9, photoImgCardS10, photoImgCardS11, photoImgCardS12, photoImgCardS13, photoImgCardC1, photoImgCardC2, photoImgCardC3, photoImgCardC4, photoImgCardC5, photoImgCardC6, photoImgCardC7, photoImgCardC8, photoImgCardC9, photoImgCardC10, photoImgCardC11, photoImgCardC12, photoImgCardC13, photoImgCardD1, photoImgCardD2, photoImgCardD3, photoImgCardD4, photoImgCardD5, photoImgCardD6, photoImgCardD7, photoImgCardD8, photoImgCardD9, photoImgCardD10, photoImgCardD11, photoImgCardD12, photoImgCardD13]
#card back photoimages
photoImgCardBack = ImageTk.PhotoImage(pathImgCardBack)
#heart card variables
imgCardH1 = tkinter.Label(scrnBlackjack, image=photoImgCardH1)
imgCardH2 = tkinter.Label(scrnBlackjack, image=photoImgCardH2)
imgCardH3 = tkinter.Label(scrnBlackjack, image=photoImgCardH3)
imgCardH4 = tkinter.Label(scrnBlackjack, image=photoImgCardH4)
imgCardH5 = tkinter.Label(scrnBlackjack, image=photoImgCardH5)
imgCardH6 = tkinter.Label(scrnBlackjack, image=photoImgCardH6)
imgCardH7 = tkinter.Label(scrnBlackjack, image=photoImgCardH7)
imgCardH8 = tkinter.Label(scrnBlackjack, image=photoImgCardH8)
imgCardH9 = tkinter.Label(scrnBlackjack, image=photoImgCardH9)
imgCardH10 = tkinter.Label(scrnBlackjack, image=photoImgCardH10)
imgCardH11 = tkinter.Label(scrnBlackjack, image=photoImgCardH11)
imgCardH12 = tkinter.Label(scrnBlackjack, image=photoImgCardH12)
imgCardH13 = tkinter.Label(scrnBlackjack, image=photoImgCardH13)
#spade card variables
imgCardS1 = tkinter.Label(scrnBlackjack, image=photoImgCardS1)
imgCardS2 = tkinter.Label(scrnBlackjack, image=photoImgCardS2)
imgCardS3 = tkinter.Label(scrnBlackjack, image=photoImgCardS3)
imgCardS4 = tkinter.Label(scrnBlackjack, image=photoImgCardS4)
imgCardS5 = tkinter.Label(scrnBlackjack, image=photoImgCardS5)
imgCardS6 = tkinter.Label(scrnBlackjack, image=photoImgCardS6)
imgCardS7 = tkinter.Label(scrnBlackjack, image=photoImgCardS7)
imgCardS8 = tkinter.Label(scrnBlackjack, image=photoImgCardS8)
imgCardS9 = tkinter.Label(scrnBlackjack, image=photoImgCardS9)
imgCardS10 = tkinter.Label(scrnBlackjack, image=photoImgCardS10)
imgCardS11 = tkinter.Label(scrnBlackjack, image=photoImgCardS11)
imgCardS12 = tkinter.Label(scrnBlackjack, image=photoImgCardS12)
imgCardS13 = tkinter.Label(scrnBlackjack, image=photoImgCardS13)
#club card variables
imgCardC1 = tkinter.Label(scrnBlackjack, image=photoImgCardC1)
imgCardC2 = tkinter.Label(scrnBlackjack, image=photoImgCardC2)
imgCardC3 = tkinter.Label(scrnBlackjack, image=photoImgCardC3)
imgCardC4 = tkinter.Label(scrnBlackjack, image=photoImgCardC4)
imgCardC5 = tkinter.Label(scrnBlackjack, image=photoImgCardC5)
imgCardC6 = tkinter.Label(scrnBlackjack, image=photoImgCardC6)
imgCardC7 = tkinter.Label(scrnBlackjack, image=photoImgCardC7)
imgCardC8 = tkinter.Label(scrnBlackjack, image=photoImgCardC8)
imgCardC9 = tkinter.Label(scrnBlackjack, image=photoImgCardC9)
imgCardC10 = tkinter.Label(scrnBlackjack, image=photoImgCardC10)
imgCardC11 = tkinter.Label(scrnBlackjack, image=photoImgCardC11)
imgCardC12 = tkinter.Label(scrnBlackjack, image=photoImgCardC12)
imgCardC13 = tkinter.Label(scrnBlackjack, image=photoImgCardC13)
#diamond card variables
imgCardD1 = tkinter.Label(scrnBlackjack, image=photoImgCardD1)
imgCardD2 = tkinter.Label(scrnBlackjack, image=photoImgCardD2)
imgCardD3 = tkinter.Label(scrnBlackjack, image=photoImgCardD3)
imgCardD4 = tkinter.Label(scrnBlackjack, image=photoImgCardD4)
imgCardD5 = tkinter.Label(scrnBlackjack, image=photoImgCardD5)
imgCardD6 = tkinter.Label(scrnBlackjack, image=photoImgCardD6)
imgCardD7 = tkinter.Label(scrnBlackjack, image=photoImgCardD7)
imgCardD8 = tkinter.Label(scrnBlackjack, image=photoImgCardD8)
imgCardD9 = tkinter.Label(scrnBlackjack, image=photoImgCardD9)
imgCardD10 = tkinter.Label(scrnBlackjack, image=photoImgCardD10)
imgCardD11 = tkinter.Label(scrnBlackjack, image=photoImgCardD11)
imgCardD12 = tkinter.Label(scrnBlackjack, image=photoImgCardD12)
imgCardD13 = tkinter.Label(scrnBlackjack, image=photoImgCardD13)
#card labels and data
cardArray = [[imgCardH1, 0, 0, 0], [imgCardH2, 2, 0, 0], [imgCardH3, 3, 0, 0], [imgCardH4, 4, 0, 0], [imgCardH5, 5, 0, 0], [imgCardH6, 6, 0, 0], [imgCardH7, 7, 0, 0], [imgCardH8, 8, 0, 0], [imgCardH9, 9, 0, 0], [imgCardH10, 10, 0, 0], [imgCardH11, 10, 0, 0], [imgCardH12, 10, 0, 0], [imgCardH13, 10, 0, 0], [imgCardS1, 0, 0, 0], [imgCardS2, 2, 0, 0], [imgCardS3, 3, 0, 0], [imgCardS4, 4, 0, 0], [imgCardS5, 5, 0, 0], [imgCardS6, 6, 0, 0], [imgCardS7, 7, 0, 0], [imgCardS8, 8, 0, 0], [imgCardS9, 9, 0, 0], [imgCardS10, 10, 0, 0], [imgCardS11, 10, 0, 0], [imgCardS12, 10, 0, 0], [imgCardS13, 10, 0, 0], [imgCardC1, 0, 0, 0], [imgCardC2, 2, 0, 0], [imgCardC3, 3, 0, 0], [imgCardC4, 4, 0, 0], [imgCardC5, 5, 0, 0], [imgCardC6, 6, 0, 0], [imgCardC7, 7, 0, 0], [imgCardC8, 8, 0, 0], [imgCardC9, 9, 0, 0], [imgCardC10, 10, 0, 0], [imgCardC11, 10, 0, 0], [imgCardC12, 10, 0, 0], [imgCardC13, 10, 0, 0], [imgCardD1, 0, 0, 0], [imgCardD2, 2, 0, 0], [imgCardD3, 3, 0, 0], [imgCardD4, 4, 0, 0], [imgCardD5, 5, 0, 0], [imgCardD6, 6, 0, 0], [imgCardD7, 7, 0, 0], [imgCardD8, 8, 0, 0], [imgCardD9, 9, 0, 0], [imgCardD10, 10, 0, 0], [imgCardD11, 10, 0, 0], [imgCardD12, 10, 0, 0], [imgCardD13, 10, 0, 0]]


#resets the cards data and their placement
def cardReset():
	global cardArray
	global playerCards
	global computerCards
	global playerTotalAlt
	global playerTotalBase
	global commputerTotal
	global computerTotalAlt
	global computerTotalBase
	global firstDraw
	playerTotal = 0
	playerTotalAlt = 0
	playerTotalBase = 0
	computerTotal = 0
	computerTotalAlt = 0
	computerTotalBase = 0
	firstDraw = True
	computerBestHand = 0
	playerBestHand = 0
	playerCards = []
	computerCards = []
	cardArray = [[imgCardH1, 0, 0, 0], [imgCardH2, 2, 0, 0], [imgCardH3, 3, 0, 0], [imgCardH4, 4, 0, 0], [imgCardH5, 5, 0, 0], [imgCardH6, 6, 0, 0], [imgCardH7, 7, 0, 0], [imgCardH8, 8, 0, 0], [imgCardH9, 9, 0, 0], [imgCardH10, 10, 0, 0], [imgCardH11, 10, 0, 0], [imgCardH12, 10, 0, 0], [imgCardH13, 10, 0, 0], [imgCardS1, 0, 0, 0], [imgCardS2, 2, 0, 0], [imgCardS3, 3, 0, 0], [imgCardS4, 4, 0, 0], [imgCardS5, 5, 0, 0], [imgCardS6, 6, 0, 0], [imgCardS7, 7, 0, 0], [imgCardS8, 8, 0, 0], [imgCardS9, 9, 0, 0], [imgCardS10, 10, 0, 0], [imgCardS11, 10, 0, 0], [imgCardS12, 10, 0, 0], [imgCardS13, 10, 0, 0], [imgCardC1, 0, 0, 0], [imgCardC2, 2, 0, 0], [imgCardC3, 3, 0, 0], [imgCardC4, 4, 0, 0], [imgCardC5, 5, 0, 0], [imgCardC6, 6, 0, 0], [imgCardC7, 7, 0, 0], [imgCardC8, 8, 0, 0], [imgCardC9, 9, 0, 0], [imgCardC10, 10, 0, 0], [imgCardC11, 10, 0, 0], [imgCardC12, 10, 0, 0], [imgCardC13, 10, 0, 0], [imgCardD1, 0, 0, 0], [imgCardD2, 2, 0, 0], [imgCardD3, 3, 0, 0], [imgCardD4, 4, 0, 0], [imgCardD5, 5, 0, 0], [imgCardD6, 6, 0, 0], [imgCardD7, 7, 0, 0], [imgCardD8, 8, 0, 0], [imgCardD9, 9, 0, 0], [imgCardD10, 10, 0, 0], [imgCardD11, 10, 0, 0], [imgCardD12, 10, 0, 0], [imgCardD13, 10, 0, 0]]
	for i in range(len(cardArray)):
		cardArray[i][0].configure(image=photoImageArray[i])
		cardArray[i][0].place(x=initialX, y=initialY)
		cardArray[i][0].configure(width=round(cardWidth), height=round(cardHeight))
		cardArray[i][2] = initialX
		cardArray[i][3] = initialY
#----------------------------------------------------
#--variables for functionality--
#variable used to lock buttons
textBoxLock = False
gameGo = True
buttonStart = False
didBet = False
firstDraw = True
endTurn = False
userAceInHand = False
computerAceInHand = False
betLock = False
yPos = 0
playerTotalText = ""
computerTotalText = ""
results = " "
resultsDelay = 5
bet = 0
#------------------------set up menu screen-----------------------
scrnTitle.configure(bg="green")

def setGameScreen():
	global balance
	global results
	if isinstance(tempBalance.get(), str) or tempBalance.get() < 1:
		lblBalError.configure(text="the balance you input is not valid.")
	else:
		results = ""
		balance = tempBalance.get()
		scrnBlackjack.tkraise()
		updateBalance()
		bettingWindow()

# Title
titleL = tkinter.Label(scrnTitle, width=20, height=20, fg="red", bg='green', font=("Helvetica", 25, "bold"), text="BlackJack")
# error info
lblBalError = tkinter.Label(scrnTitle, text="Enter the starting amount.", font=("Helvetica", 13, "bold"), bg="green")
# Currency
txtCurrency = tkinter.Entry(scrnTitle, textvariable=tempBalance)
# Play Button
btnStart = tkinter.Button(scrnTitle, width=8, height=1, bg="Blue", font=("Helvetica", 15, "bold"), activebackground="green", text="Start", fg="white", command=setGameScreen)
# Placement
titleL.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

txtCurrency.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

btnStart.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

lblBalError.place(relx =0.5, rely=0.35, anchor=tkinter.CENTER)
#-------------------------set up game functions-------------------
cardReset()

def updateBalance():
  txtBalance.configure(text = "Your current balance is:\n $" + str(balance))

#playCards are the cards of the person in turn
def cardDraw(playCards):
	global yPos
	global playerCardYPos
	global playerTotal
	global playerTotalAlt
	global playerTotalBase
	global playerBestHand
	global computerCardYPos
	global computerTotal
	global computerTotalAlt
	global computerTotalBase
	global computerBestHand
	global computerHiddenValue
	global firstDraw
	global computerTotalText
	global playerTotalText
	#y axis position of the cards
	total = 0
	alt = 0
	base = 0
	best = 0
	#sets the y position based on whose cards are being dealt
	if playCards == playerCards:
		yPos = playerCardYPos
		alt = playerTotalAlt
		total = playerTotal
		base = playerTotalBase
		best = playerBestHand
	elif playCards == computerCards:
		yPos = computerCardYPos
		alt = computerTotalAlt
		total = computerTotal
		base = computerTotalBase
		best = computerBestHand
	#gets the amount of cards in play for that player
	cardCount = len(playCards)
	#gets the width of half a card
	halfCard = cardWidth / 2
	#selects a random card
	randomNum = random.randrange(len(cardArray))
	#applies that card to a temporary variable
	tempCard = cardArray[randomNum]
	#removes that card from the deck
	cardArray.pop(randomNum)
	#adds that card to the player's hand
	playCards.append(tempCard)
	#configuring the cards data for the position
	xPos = (xGeo / 2) + (cardCount * halfCard)
	playCards[-1][2] = xPos
	playCards[-1][3] = yPos
	#places the card on the right most position
	playCards[-1][0].place(x = xPos, y = yPos)
	#add to base total
	base = base + playCards[-1][1]
	#dealing with aces
	aces = 0
	if playCards == computerCards:
		if computerHiddenValue == 0:
			aces = aces - 1
	for i in range(len(playCards)):
		if playCards[i][1] == 0:
			aces += 1
	if aces == 1:
		alt = base + 11
		total = base + (aces - 1)
	else:
		alt = base + 11
		total = base + (aces)
	if playCards == computerCards:
		if computerTotalAlt != 0:
			#checking the total with Ace as 11 and the rest as 1s
			if computerTotal > computerTotalAlt and computerTotal + computerHiddenValue > 15:
				tempCompTotal = computerTotal
				#checking the total with aces as 1s
			else:
				tempCompTotal = computerTotalAlt
		else:
			tempCompTotal = computerTotal
		if aces > 0 and alt <= 21:
			computerTotalText = "(" + str(total) + " / " + str(alt) + " + ?)"
		else:
			computerTotalText = "(" + str(total) + " + ?)"
	if playCards == playerCards:
		if aces > 0 and alt <= 21:
			playerTotalText = "(" + str(total) + " / " + str(alt) + ")"
		else:
			playerTotalText = "(" + str(total) + ")"
	if alt > total and alt <= 21:
		best = alt
	else:
		best = total
	#makes sure that the first draw of the computer has their card hidden
	if firstDraw and playCards == computerCards:
		playCards[-1][0].configure(image=photoImgCardBack)
		computerHiddenValue = playCards[-1][1]
		base = base - computerHiddenValue
		firstDraw = False
	if playCards == playerCards:
		playerTotalAlt = alt
		playerTotal = total
		playerTotalBase = base
		playerBestHand = best
	elif playCards == computerCards:
		computerTotalAlt = alt
		computerTotal = total
		computerTotalBase = base
		computerBestHand = best
	#recenters all the cards  in hand
	for i in range(len(playCards)):
		playCards[i][0].place(x=playCards[i][2] - halfCard, y=playCards[i][3])
		playCards[i][2] = playCards[i][2] - halfCard
	if playCards == computerCards:
		txtComputerTotal.configure(text = str(computerTotalText))
	else:
		txtPlayerTotal.configure(text = str(playerTotalText))

def endGameCheck():
  if balance < 1:
    scrnStats.tkraise()
    lostL.configure(text="Rounds Lost: " + str(roundsLost))
    wonL.configure(text="Rounds Won: " + str(roundsWon))

def lockButtons():
  btnHit.configure(state = tkinter.DISABLED)
  btnStand.configure(state = tkinter.DISABLED)

def unlockButtons():
  btnHit.configure(state = tkinter.NORMAL)
  btnStand.configure(state = tkinter.NORMAL)

#blackjack
def blackjack():
  global balance
  global results
  global roundsWon
  balance = balance + round(bet * 1.5)
  results = "Blackjack!"
  roundsWon += 1
  cardReset()
  endGameCheck()
  bettingWindow()
  
#bust
def bust():
  global balance
  global results
  global roundsLost
  balance = balance - bet
  updateBalance()
  results = "Bust!"
  roundsLost += 1
  cardReset()
  endGameCheck()
  bettingWindow()

#computer wins
def computerWins():
  global balance
  global results
  global roundsLost
  balance = balance - bet
  updateBalance()
  results = "Dealer Wins!"
  roundsLost += 1
  cardReset()
  endGameCheck()
  bettingWindow()

#push
def push():
  global results
  results = "Push!"
  cardReset()
  endGameCheck()
  bettingWindow()

#player wins
def playerWins():
  global balance
  global results
  global roundsWon
  balance = balance + bet
  updateBalance()
  results = "Player Wins!"
  roundsWon += 1
  cardReset()
  endGameCheck()
  bettingWindow()
  
#check blackjack or bust
def checkBlackjackBust():
  if playerBestHand == 21:
    blackjack()
  elif playerBestHand > 21:
    bust()

#check winner
def checkWinner():
  #get dealer blackjack better hand than player and pl
  if computerBestHand > playerBestHand and computerBestHand < 22:
    computerWins()
  elif computerBestHand == playerBestHand and playerBestHand < 22:
    push()
  else:
    playerWins()

#initial draw fucnton
def initialDraw():
  global results
  results = ""
  cardReset()
  while len(playerCards) > 2 or len(playerCards) < 2:
    for i in range(2):
      cardDraw(playerCards)
      cardDraw(computerCards)

def stand():
	#computer is drawing cards as long as his card value total is less than or equal to 15
	while computerBestHand <= 15:
		cardDraw(computerCards)
	txtComputerTotal.configure(text = "(" + str(computerBestHand) + ")")
	checkWinner()
	firstDraw = True

def hit():
  cardDraw(playerCards)
  checkBlackjackBust()

#--betting window--
def errorWindowDestroy():
	global betError
	betError.destroy()

def bettingError():
	global betError
	betError = tkinter.Toplevel(main)
	betError.title("Error")
	tkinter.Label(betError, text="The betting amount you input is invalid. Try again.").pack()
	betError.protocol("WM_DELETE_WINDOW", on_closing)
	tkinter.Button(betError, text="okay", command=errorWindowDestroy).pack()


def on_closing():
	pass


def betWindowDestroy(window):
	global betWindow
	global betLock
	global bet
	#checking to see if the betting amount is viable
	if betLock == False:
		betLock = True
		if tempBet.get() < 1 or tempBet.get() > balance or isinstance(tempBet.get(), str):
			bettingError()
		else:
			unlockButtons()
			didBet = True
			initialDraw()
			window.destroy()
			bet = tempBet.get()
		betLock = False

def bettingWindow():
	global betWindow
	lockButtons()
	if betLock == False and balance > 0:
		# Toplevel object which will
		# be treated as a new window
		betWindow = tkinter.Toplevel(main)
		# sets the title of the
		# Toplevel widget
		betWindow.title("Betting")
		#makes it to where the window is unclosable
		betWindow.protocol("WM_DELETE_WINDOW", on_closing)
		tkinter.Label(betWindow, text="Your current balance is:\n $" + str(balance)).pack()
		lblBetInfo = tkinter.Label(betWindow, text="Type your betting amount").pack()
		tkinter.Entry(betWindow, textvariable=tempBet).pack()
		if results == "Blackjack!" or results == "Player Wins!":
			tkinter.Label(betWindow, text = results, fg="green").pack()
		elif results == "Bust!" or results == "Dealer Wins!":
			tkinter.Label(betWindow, text = results, fg="red").pack()
		else:
			tkinter.Label(betWindow, text = results, fg = "yellow").pack()
		tkinter.Button(betWindow, text="Bet", activebackground = "green", command=lambda: betWindowDestroy(betWindow)).pack()

#---  -------------------set up game screen---------------------
#not placed yet
scrnBlackjack.configure(bg="green")
txtBalance = tkinter.Label(scrnBlackjack, font=("Helvetica", 12, "bold"), text="Your balance is: " + str(balance), bg="green")
txtPlayerTotal = tkinter.Label(scrnBlackjack, font=("Helvetica", 12, "bold"), text="0", bg="green")
txtComputerTotal = tkinter.Label(scrnBlackjack, font=("Helvetica", 12, "bold"), text="0", bg="green")
btnHit = tkinter.Button(scrnBlackjack, text="Hit", bg="red", command=hit)
btnStand = tkinter.Button(scrnBlackjack, text="Stand", bg="blue", command=stand)
lblPLayerTotal = tkinter.Label(scrnBlackjack, text = "(" + ")")
btnHit.place(relx=0.1, rely=0.5, anchor=tkinter.CENTER)
btnStand.place(relx=0.9, rely=0.5, anchor=tkinter.CENTER)
txtBalance.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
txtPlayerTotal.place(relx=0.44, rely=0.9)
txtComputerTotal.place(relx=0.41, rely=0.03)
#-----------------set up end screen---------------------
scrnStats.configure(bg="green")

# Reset to Title Screen
def resetScrnTitle():
  global roundsWon
  global roundsLost
  roundsWon = 0
  roundsLost = 0
  cardReset()
  scrnTitle.tkraise()

# Labels
gameOverL = tkinter.Label(scrnStats, width=20, height=20, fg="red", bg='green', font=("Helvetica", 20, "bold"), text="Game Over")
wonL = tkinter.Label(scrnStats, width=13, height=1, fg='white', bg='green', font=("Helvetica", 15, "italic"), text="Rounds Won: " + str(roundsWon))
lostL = tkinter.Label(scrnStats, width=13, height=1, fg='white', bg='green', font=("Helvetica", 15, "italic"), text="Rounds Lost: " + str(roundsLost))
# Buttons
playB = tkinter.Button(scrnStats, width=8, height=2, fg='white', bg="blue", activebackground='green', font=("Helvetica", 15, "bold"), text='Play Again!', command=resetScrnTitle)

# Placement
gameOverL.place(relx=0.3, rely=0.4, anchor=tkinter.CENTER)
wonL.place(relx=0.75, rely=0.4, anchor=tkinter.CENTER)
lostL.place(relx=0.75, rely=0.6, anchor=tkinter.CENTER)
playB.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)

#start window loop
main.mainloop()
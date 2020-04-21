import tkinter
import random
import time
from tkinter import messagebox as mb


def load_cards(card):
    suits = ['club', 'diamond', 'heart', 'spade']
    faced_cards = ['jack', 'queen', 'king']

    for suit in suits:
        for number in range(1, 11):
            image = tkinter.PhotoImage(file='cards/{}_{}.png'.format(number, suit))
            card.append((number, image))

        for faced_card in faced_cards:
            image = tkinter.PhotoImage(file='cards/{}_{}.png'.format(faced_card, suit))
            card.append((10, image))


def hit(frame):
    card = deck.pop(0)
    deck.append(card)
    tkinter.Label(frame, image=card[1], bg='green').pack(side='left')
    return card


def hit_player():
    card = hit(player_card_frame)
    player_hands[0].append(str(card[0]))
    card_value = card[0]
    # Add 11 if card is Ace and Ace is not found in player's hand
    if card_value == 1 and 1 not in player_hands[0]:
        card_value = 11

    player_hands[1] += card_value
    player_score_label.set(player_hands[1])

    # Check players status after each hit
    if player_hands[1] > 21:
        display_result('Lost', 'You bust!')
    elif player_hands[1] == 21:
        display_result('Won', 'Black Jack')


def hit_dealer():
    card = hit(dealer_card_frame)
    dealer_hands[0].append(card[0])
    card_value = card[0]
    # Add 11 if card is Ace and Ace is not found in dealer's hand
    if card_value == 1 and 1 not in dealer_hands[0]:
        card_value += 11

    dealer_hands[1] += card_value
    dealer_score_label.set(dealer_hands[1])


def stand():
    score_to_beat = player_hands[1]
    dealer_score = dealer_hands[1]
    while dealer_score < score_to_beat:
        hit_dealer()
        dealer_score = dealer_hands[1]

    dealer_score_label.set(dealer_score)

    # Check dealer's status
    if dealer_score > 21:
        display_result('Won', "Dealer Bust!")
    elif dealer_score == score_to_beat:
        display_result('Tie', "You tied with the dealer")
    else:
        display_result("Lost", "Dealer won!")


def display_result(title, message):
    result_variable.set(message)
    mb.showinfo(title=title, message=message)
    hit_button['state']='disable'
    stand_button['state'] = 'disable'


def new_game():
    global dealer_card_frame
    global player_card_frame
    global deck

    # Clear cards from frame
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, relief="sunken", bg='green')
    dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky="w")

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, relief='sunken',  bg='green')
    player_card_frame.grid(row=2, column=1, rowspan=2, sticky="w")

    # Reset result variable and buttons
    result_variable.set('')
    hit_button['state']='normal'
    stand_button['state'] = 'normal'

    random.shuffle(deck)
    # Clear hands
    player_hands[0].clear()
    player_hands[1] = 0
    dealer_hands[0].clear()
    dealer_hands[1] = 0

    # Hit dealer with one card in the beginning
    hit_dealer()

    # Hit player with two cards to begin
    for i in range(0,2):
        hit_player()


mainWindow = tkinter.Tk()
mainWindow.title('Black Jack')
mainWindow.geometry('430x300+500+150')


result_variable = tkinter.StringVar()
tkinter.Label(mainWindow, textvariable=result_variable).grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, bg="green")
card_frame.grid(row=1, column=0,  columnspan=3, rowspan=2, sticky='we')

dealer_card_frame = tkinter.Frame(card_frame, relief="sunken", bg='green')
dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky="w")

player_card_frame = tkinter.Frame(card_frame, relief='sunken',  bg='green')
player_card_frame.grid(row=2, column=1, rowspan=2, sticky="w")

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", bg='green').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, bg='green').grid(row=1, column=0)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", bg='green').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, bg='green').grid(row=3, column=0)


button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

# Hit button
hit_button = tkinter.Button(button_frame, text="Hit", command=hit_player, width=5)
hit_button.grid(row=0, column=0)

# Stand button
stand_button = tkinter.Button(button_frame, text="Stand", command=stand, width=6)
stand_button.grid(row=0, column=1)

# New Game Button
tkinter.Button(button_frame, text="New Game", command=new_game).grid(row=0, column=2)

cards = []
load_cards(cards)
deck = list(cards)

player_hands = [[], 0]
dealer_hands = [[], 0]
new_game()

mainWindow.mainloop()
import random
from player import Player

deck = ['A',2,3,4,5,6,7,8,9,10,'J', 'Q', 'K'] * 4
letter_cards ={'A':1,
               'J': 10,
               'Q': 10,
               'K': 10}

"""
Flow of game:
Load card images
Deal player and cpu 2 cards
2 options are given:
    - Hitting
        * check if player goes over 21 after every hit
        * if the player goes over , then the player lose
    - Standing
        * check against computer card to see whose number is higher
        * if number is higher then win ,and vice versa

3# 
"""

class BlackJack:

    def __init__(self):
        self.player = self.deal()
        self.cpu = self.deal()

    def deal(self):
        hand = [[], 0]
        random.shuffle(deck)
        for i in range(0, 2):
            self.hit(hand)
        return hand

    def hit(self, player):
        card = deck.pop()
        if card in letter_cards:
            card_value = letter_cards[card]
            player[1] += card_value
        else:
            player[1] += card
        player[0].append(card)


    def stand(self, player_sum):
        cpuSum = self.cpu[1]
        while cpuSum <= player_sum & cpuSum < 21:
            self.hit(self.cpu)
            cpuSum += self.cpu[1]

        if cpuSum <= 21 & cpuSum > player_sum :
            print("Cpu won!  {}".format(self.cpu[0]))
        else:
            print("Cpu bust!  {}\nYou won!  {}".format(self.cpu[0], self.player[0]))

    def display_cards(self):
        print("\t\tCpu Hand: [{}, hidden ]\n\t\tYour Hand:{}".format(self.cpu[0][0], self.player[0]))

    def play(self):
        prompt = ''
        while prompt != 'q':
            self.display_cards()
            player_sum = self.player[1]

            if  player_sum < 21:  # If player is still under 21
                prompt = input("Would you like to Hit(H) or Stand(S)? ")
                if prompt.upper() == 'H':
                    self.hit(self.player)  # Hit
                elif prompt.upper() == 'L':
                    self.stand(self.player[1])  # Stand
                    break;
                else:
                    print("Please choose either H or L")

            elif player_sum > 21:  # If player goes over 21
                print("\nYou bust, you lose. {}".format(self.player[0]))
                break;

            elif player_sum == 21:  # If player hits 21
                print("\nCongratz you hit 21")
                break;





b = BlackJack()
b.play()

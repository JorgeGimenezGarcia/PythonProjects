'''
Code created by Jorge Gimenez Garcia
If you dont know what is War, this is the link to the Wikipedia.
link: https://en.wikipedia.org/wiki/War_(card_game)
'''

import random

#We create a simple way to create cards
#Hearts,Diamonds,Spades,Clubs
SUITE='H D S C'.split()
RANKS='2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    def __init__(self):
        print("Creating New Ordered Deck!")
        self.cards=[(s,r)for s in SUITE for r in RANKS]
        
    
    #Show the cards
    def show(self):
        for c in self.cards:
            c.show()

    def randomShuffle(self):
        print("Shuffling Deck")
        random.shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()
   
    def splittingHalf(self):
        #We return the first 26 cards, and the last 26
        return(self.cards[:26], self.cards[26:])
    
    pass

class Hand:
    #Should be a method to add and remove card here
    def __init__(self,cards):
        self.cards = cards
    
    def __str__(self):
        return "Contains {} cards".format(len(self.cards))
    
    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

    pass

class Player:
    #This should take a instance of a Hand
    def __init__(self,name,hand):
        self.name=name
        self.hand=hand
    
    def play_card(self):
        drawn_card=self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards=[]
        if len(self.hand.cards)<3:
            return self.hand.cards
        else:
            #In the rules if its a war we should remove the first 3 cards
            for x in range(3):
                war_cards.append(self.hand.remove_card())

            return war_cards
        
    def still_has_cards(self):
        #Returns True if player still has cards left
        return len(self.hand.cards)!=0
    

    pass

def loopGame(user,computer,total_rounds,war_count):

    while user.still_has_cards() and computer.still_has_cards():
        total_rounds+=1
        print("Time for a new round!")
        print("Here are the current standings")
        print(user.name+" has the count: "+ str(len(user.hand.cards)))
        print(computer.name+" has the count: "+ str(len(computer.hand.cards)))
        print("Play a card!")
        print("\n")

        table_cards=[]

        c_card=computer.play_card()
        p_card=user.play_card()

        table_cards.append(c_card)
        table_cards.append(p_card)

        #We do this check to look the range first
        if c_card[1]==p_card[1]:
            war_count+=1
            print("WAR!")

            table_cards.extend(user.remove_war_cards())
            table_cards.extend(computer.remove_war_cards())

            if RANKS.index(c_card[1])< RANKS.index(p_card[1]):
                user.hand.add(table_cards)
            else:
                computer.hand.add(table_cards)
        
        else:
            if RANKS.index(c_card[1])<RANKS.index(p_card[1]):
                user.hand.add(table_cards)
            else:
                computer.hand.add(table_cards)
    
    return(total_rounds, war_count)


#Logic of the Game
def Game():
   
    print("Welcome to War, let's begin...")

    #We create a new deck and we shuffle it
    deck=Deck()
    deck.randomShuffle()

    #We create 2 variables to save the halfs of the deck
    half1,half2=deck.splittingHalf()

    #We create both players
    computer=Player("computer",Hand(half1))

    name =input("What is your name?")
    user=Player(name,Hand(half2))
    total_rounds=0
    war_count=0
    total_rounds,war_count=loopGame(user,computer,total_rounds,war_count)

    print("Game over, number of rounds: "+ str(total_rounds))
    print("A war happened "+str(war_count)+"times")

if __name__ == "__main__":
    Game()
